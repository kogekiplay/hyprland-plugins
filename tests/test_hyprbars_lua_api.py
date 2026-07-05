from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class HyprbarsLuaApiTest(unittest.TestCase):
    def test_lua_api_can_clear_buttons_before_readding_them(self):
        main_cpp = (ROOT / "hyprbars" / "main.cpp").read_text()

        self.assertIn("int newLuaClearButtons(lua_State* L)", main_cpp)
        self.assertIn("g_pGlobalState->buttons.clear();", main_cpp)
        self.assertIn('addLuaFunction(PHANDLE, "hyprbars", "clear_buttons", ::newLuaClearButtons)', main_cpp)


if __name__ == "__main__":
    unittest.main()
