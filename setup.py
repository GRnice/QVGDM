from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "Qui Veut Gagner Des Millions",
    version = "1.1",
    description = "QVGDM",
    executables = [Executable("./Main.py")],
)