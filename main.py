
def define_env(env):
    print("✅ main.py chargé")

    @env.macro
    def test_macro():
        return "macro OK"


