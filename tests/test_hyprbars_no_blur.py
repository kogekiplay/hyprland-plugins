from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class HyprbarsNoBlurTest(unittest.TestCase):
    def test_bar_blur_respects_window_no_blur_rule(self):
        bar_deco_cpp = (ROOT / "hyprbars" / "barDeco.cpp").read_text()
        bar_pass_cpp = (ROOT / "hyprbars" / "BarPassElement.cpp").read_text()

        self.assertIn("m_ruleApplicator->noBlur().valueOrDefault()", bar_deco_cpp)
        self.assertIn("m_ruleApplicator->noBlur().valueOrDefault()", bar_pass_cpp)


if __name__ == "__main__":
    unittest.main()
