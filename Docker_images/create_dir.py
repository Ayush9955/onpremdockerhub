import os

directories = ["node", "react", "vue", "angular", "django", "flask", "nginx", "perl", "ruby", "fastapi", "java", "golang", "dotnet", "html", "php"]

for directory in directories:
    os.makedirs(directory, exist_ok=True)
