from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


class HyprbarsInputTest(unittest.TestCase):
    def test_titlebar_geometry_can_accept_input_when_window_hit_test_misses(self):
        bar_deco_cpp = (ROOT / "hyprbars" / "barDeco.cpp").read_text()
        bar_deco_hpp = (ROOT / "hyprbars" / "barDeco.hpp").read_text()

        self.assertIn("cursorIsInsideBar()", bar_deco_hpp)
        self.assertRegex(
            bar_deco_cpp,
            re.compile(
                r"bool\s+CHyprBar::cursorIsInsideBar\(\).*?"
                r"VECINRECT\s*\(\s*COORDS\s*,\s*0\s*,\s*0\s*,\s*assignedBoxGlobal\(\)\.w\s*,\s*HEIGHT\s*-\s*1\s*\)",
                re.S,
            ),
        )

        input_is_valid = re.search(r"bool\s+CHyprBar::inputIsValid\(\)\s*\{(?P<body>.*?)\n\}", bar_deco_cpp, re.S)
        self.assertIsNotNone(input_is_valid)
        body = input_is_valid.group("body")

        self.assertIn("const bool CURSORINSIDEBAR = cursorIsInsideBar();", body)
        self.assertIn("if (CURSORINSIDEBAR)\n        return true;", body)
        self.assertLess(body.index("if (CURSORINSIDEBAR)"), body.index("WINDOWATCURSOR != m_pWindow"))


if __name__ == "__main__":
    unittest.main()
