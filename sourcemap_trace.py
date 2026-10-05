"""Trace a generated position through a flat v3 source map offline."""
import argparse,json,pathlib
ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
def decode(segment):
    out=[];value=shift=0
    for char in segment:
        if char not in ALPHABET:raise ValueError('invalid base64 VLQ character')
        digit=ALPHABET.index(char);value|=(digit&31)<<shift
        if digit&32:
            shift+=5
            if shift>35:raise ValueError('VLQ integer too large')
        else:
            if value>=2**32:raise ValueError('VLQ integer exceeds 32 bits')
            out.append(-2**31 if value==1 else (-(value>>1)if value&1 else value>>1));value=shift=0
    if shift:raise ValueError('unterminated VLQ')
    return out

def trace(source_map,line,column):
    if type(line)is not int or line<1 or type(column)is not int or column<0:raise ValueError('line is 1-based; column is 0-based')
    if not isinstance(source_map,dict)or source_map.get('version')!=3 or 'sections'in source_map:raise ValueError('only flat v3 source maps supported')
    sources=source_map.get('sources');names=source_map.get('names',[]);mappings=source_map.get('mappings')
    if not isinstance(sources,list)or not all(isinstance(x,str)for x in sources)or not isinstance(names,list)or not all(isinstance(x,str)for x in names)or not isinstance(mappings,str):raise ValueError('invalid sources, names or mappings')
    if len(mappings)>5_000_000:raise ValueError('mapping limit exceeded')
    src=original_line=original_col=name=0;found=None
    for number,text in enumerate(mappings.split(';'),1):
        generated=0;last=-1
        for segment in text.split(',')if text else []:
            vals=decode(segment)
            if len(vals)not in (1,4,5):raise ValueError('segment needs 1, 4 or 5 fields')
            generated+=vals[0]
            if generated<0 or generated<=last:raise ValueError('generated columns must be strictly increasing')
            last=generated;position=None
            if len(vals)>1:
                src+=vals[1];original_line+=vals[2];original_col+=vals[3]
                if not 0<=src<len(sources)or original_line<0 or original_col<0:raise ValueError('source position out of range')
                if len(vals)==5:
                    name+=vals[4]
                    if not 0<=name<len(names):raise ValueError('name out of range')
                position={'source':sources[src],'line':original_line+1,'column':original_col,'name':names[name]if len(vals)==5 else None,'generated_column':generated}
            if number==line and generated<=column:found=position
    return found

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('map');p.add_argument('line',type=int);p.add_argument('column',type=int);a=p.parse_args()
    try:
        with pathlib.Path(a.map).open('rb')as f:raw=f.read(10_000_001)
        if len(raw)>10_000_000:raise ValueError('10 MB source map limit exceeded')
        r=trace(json.loads(raw),a.line,a.column);print(json.dumps({'original':r}));return 0 if r is not None else 1
    except (ValueError,OSError,TypeError,RecursionError)as e:print(json.dumps({'error':str(e)}));return 2
if __name__=='__main__':raise SystemExit(main())
