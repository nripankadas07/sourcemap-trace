import unittest
from sourcemap_trace import trace,decode
def sm(mapping):return {'version':3,'sources':['a.js','b.js'],'names':['fn'],'mappings':mapping}
class Tests(unittest.TestCase):
 def test_signed_minimum(self):self.assertEqual(decode('B'),[-2147483648])
 def test_integer_overflow(self):
  with self.assertRaises(ValueError):decode('ggggggE')
 def test_exact_named(self):self.assertEqual(trace(sm('AAAAA'),1,0),{'source':'a.js','line':1,'column':0,'name':'fn','generated_column':0})
 def test_lower_bound(self):self.assertEqual(trace(sm('AAAA,KACE'),1,6)['column'],2)
 def test_lines_and_negative_delta(self):
  r=trace(sm('ACCE;ADDF'),2,0);self.assertEqual(r['source'],'a.js');self.assertEqual(r['line'],1);self.assertEqual(r['column'],0)
 def test_unmapped_resets(self):self.assertIsNone(trace(sm('AAAA,K'),1,6))
 def test_before_first(self):self.assertIsNone(trace(sm('KAAA'),1,0))
 def test_missing_line(self):self.assertIsNone(trace(sm('AAAA'),2,0))
 def test_invalid_vlq(self):
  for s in ['g','!','AAAAAAAAAA']:
   with self.assertRaises(ValueError):trace(sm(s),1,0)
 def test_section_rejected(self):
  m=sm('AAAA');m['sections']=[]
  with self.assertRaises(ValueError):trace(m,1,0)
 def test_source_bounds(self):
  with self.assertRaises(ValueError):trace(sm('AEAA'),1,0)
