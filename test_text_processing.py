from engfmt import all_to_eng_fmt, all_from_eng_fmt, set_preferences

class TestCase:
    def __init__(self, name, eng, flt):
        self.name = name
        self.eng = eng
        self.flt = flt

test_cases = [
    TestCase('chirp', '1mA', '1e-3A'),
    TestCase('bungler', 'blah 1mA', 'blah 1e-3A'),
    TestCase('dilute', 'blah 1mA.', 'blah 1e-3A.'),
    TestCase('pelvis', 'blah 1mA blah', 'blah 1e-3A blah'),
    TestCase('tickle', '-1mA', '-1e-3A'),
    TestCase('wrangle', 'blah -1mA', 'blah -1e-3A'),
    TestCase('accessory', 'blah -1mA.', 'blah -1e-3A.'),
    TestCase('observer', 'blah -1mA blah', 'blah -1e-3A blah'),
    TestCase('meadow', 'blah ipn_250nA.', 'blah ipn_250nA.'),
]

names = set()
def test_text_processing():
    set_preferences(spacer='')
    for case in test_cases:
        assert case.name not in names
        names.add(case.name)
        assert case.eng == all_to_eng_fmt(case.flt), case.name
        assert all_from_eng_fmt(case.eng) == case.flt, case.name
