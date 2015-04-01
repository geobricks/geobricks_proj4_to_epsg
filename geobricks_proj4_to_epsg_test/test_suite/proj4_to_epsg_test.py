import unittest
from geobricks_proj4_to_epsg.core.proj4_to_epsg import get_epsg_code_from_proj4, get_proj4_json_from_epsg_code, get_epsg_code_from_proj4_json



class GeobricksTest(unittest.TestCase):

    # TODO: the result is different from http://spatialreference.org/ref/epsg/4326/proj4/
    # +proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs
    def test_epsg_from_proj4_4326(self):
        epsg = get_epsg_code_from_proj4('+proj=longlat +datum=WGS84 +no_defs')
        self.assertEqual(str(epsg), '4326')

    def test_get_proj4_from_4326(self):
        result = get_proj4_json_from_epsg_code(4326)
        self.assertEqual(result, {u'no_defs': True, u'datum': u'WGS84', u'proj': u'longlat'})

    def test_get_epsg_code_from_proj4(self):
        epsg = get_epsg_code_from_proj4('+datum=WGS84 +lat_ts=30 +lon_0=0 +no_defs +proj=cea +units=m +x_0=0 +y_0=0')
        self.assertEqual('3975', str(epsg))

    def test_get_proj4_json_from_epsg_code(self):
        proj4_json = get_proj4_json_from_epsg_code(3975)
        self.assertEqual(proj4_json, {u'lon_0': u'0', u'datum': u'WGS84', u'y_0': u'0', u'no_defs': True, u'proj': u'cea', u'x_0': u'0', u'units': u'm', u'lat_ts': u'30'})

    def test_get_epsg_code_from_proj4_json(self):
        epsg = get_epsg_code_from_proj4_json({u'lon_0': u'0', u'datum': u'WGS84', u'y_0': u'0', u'no_defs': True, u'proj': u'cea', u'x_0': u'0', u'units': u'm', u'lat_ts': u'30'})
        self.assertEqual('3975', str(epsg))

    # def test_new_test(self):
    #     epsg = get_epsg_code_from_proj4('+datum=WGS84 +k=1 +lon_0=0 +no_defs +proj=merc +units=m +x_0=0 +y_0=0')
    #     print epsg
    #     self.assertEqual(str(epsg), '3857')
    # def test_new_test2(self):
    #     result = get_proj4_json_from_epsg_code(3857)
    #     print result
    #     self.assertEqual(str(result), '3975')

    def test_get_proj4_json_from_epsg_code_3957(self):
        epsg = get_epsg_code_from_proj4('+proj=cea +lon_0=0 +lat_ts=30 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs')
        self.assertEqual(str(epsg), '3975')


def run_test():
    suite = unittest.TestLoader().loadTestsFromTestCase(GeobricksTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    run_test()
