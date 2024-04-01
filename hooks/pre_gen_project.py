import subprocess
import json

def run_pre_hook():
    # Leer las variables de la plantilla desde el archivo cookiecutter.json
    with open("/home/gerardo19/plantillas_proyectos_cd/cookiecutter.json") as f:
        variables = json.load(f)

    # Obtener los valores de nombre y correo electrónico del autor del proyecto
    author_name = variables.get("project_author_name")
    author_email = variables.get("project_author_email")

    # Configurar el nombre y correo electrónico del autor en Git
    subprocess.run(["git", "config", "user.name", author_name])
    subprocess.run(["git", "config", "user.email", author_email])
    
    # Inicializar el repositorio Git
    subprocess.run(["git", "init"])
    
    # Agregar todos los archivos al repositorio
    subprocess.run(["git", "add", "."])

    # Realizar el primer commit
    subprocess.run(["git", "commit", "-m", "Primer commit"])

if __name__ == "__main__":
    run_pre_hook()