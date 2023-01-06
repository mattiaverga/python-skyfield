from skyfield import api
from skyfield.data.hipparcos import load_dataframe

def test_dataframe():
    with api.load.open('hip_main.dat.gz') as f:
        df = load_dataframe(f)
    star = api.Star.from_dataframe(df)
    assert repr(star) == 'Star(ra shape=9933, dec shape=9933, ra_mas_per_year shape=9933, dec_mas_per_year shape=9933, parallax_mas shape=9933, epoch shape=9933)'

def test_from_ongc():
    hercules = api.Star.from_ongc('M13')
    assert repr(hercules) == (
        'Star(ra=250.42345833333337, dec=36.46130555555556, ra_mas_per_year=-3.18, '
        'dec_mas_per_year=-2.56, parallax_mas=0.0813, epoch=2451545.0)'
    )
