def template():
    template_dict ={"node":'''\
    FROM ${base_image}:${base_version}
    
    WORKDIR /oortfy
    
    COPY . /oortfy
    
    RUN if [ "$PACKAGE_MANAGER" = "yarn" ]; then yarn; else npm install; fi
    
    EXPOSE ${port}
    
    CMD if [ "$PACKAGE_MANAGER" = "yarn" ]; then yarn start; else npm start; fi
    ''',
    
    "react":'''\
    FROM ${base_image}:${base_version}
    
    WORKDIR /oortfy
    
    COPY . /oortfy
    
    RUN if [ "$PACKAGE_MANAGER" = "yarn" ]; then yarn; else npm install; fi
    
    RUN npm install react-scripts@${react_base_version} -g --silent
    
    EXPOSE ${port}
    
    CMD if [ "$PACKAGE_MANAGER" = "yarn" ]; then yarn start; else npm start; fi
    ''',
    
    "vue":'''\
    FROM ${base_image}:${base_version}
    
    WORKDIR /oortfy
    
    COPY . /oortfy
    
    RUN if [ "$PACKAGE_MANAGER" = "yarn" ]; then yarn; else npm install; fi
    
    RUN npm install -g @vue/cli
    
    EXPOSE ${port}
    
    CMD if [ "$PACKAGE_MANAGER" = "yarn" ]; then yarn serve; else npm run serve; fi
    ''',
    
    "angular":'''\
    FROM ${base_image}:${base_version}
    
    WORKDIR /oortfy
    
    COPY . /oortfy
    
    RUN if [ "$PACKAGE_MANAGER" = "yarn" ]; then yarn; else npm install; fi
    
    RUN ${package_manager} install -g @angular/cli
    
    EXPOSE ${port}
    
    CMD if [ "$PACKAGE_MANAGER" = "yarn" ]; then yarn start; else npm start; fi
    ''',
    
    "django":'''\
    FROM ${base_image}:${base_base_version}
    
    ENV PYTHONUNBUFFERED=1
    
    WORKDIR /oortfy
    
    COPY requirements.txt .
    
    RUN ${package_manager} install --no-cache-dir -r requirements.txt
    
    COPY . .
    
    EXPOSE ${port}
    
    CMD ["python", "manage.py", "runserver", "0.0.0.0:${port}"]
    ''',
    
    "flask":'''\
    FROM ${base_image}:${base_base_version}
    
    ENV PYTHONUNBUFFERED=1
    
    WORKDIR /oortfy
    
    COPY requirements.txt .
    
    RUN ${PACKAGE_MANAGER} install --no-cache-dir -r requirements.txt
    
    COPY . .
    
    EXPOSE ${port}
    
    CMD ["python", "oortfy.py"]
    ''',
    
    "nginx":'''\
    FROM ${base_image}:${base_version}
    
    COPY nginx.conf /etc/nginx/conf.d/default.conf
    
    WORKDIR /oortfy
    
    COPY . .
    
    EXPOSE ${port}
    ''',
    
    "perl":'''\
    FROM ${base_image}:${base_version}
    
    WORKDIR /oortfy
    
    COPY cpanfile* /oortfy/
    
    RUN cpanm --installdeps --notest .
    
    COPY . .
    
    EXPOSE ${port}
    
    CMD ["plackup", "-p", "${port}", "--host", "0.0.0.0", "--access-log", "/dev/null", "--error-log", "/dev/null", "--server", "Twiggy", "oortfy.psgi"]
    ''',
    
    "fastapi":'''\
    FROM tiangolo${base_image}:${base_version}
    
    COPY requirements.txt .
    
    RUN pip install --no-cache-dir -r requirements.txt
    
    COPY . .
    
    EXPOSE ${port}
    ''',
    
    "java":'''\
    FROM ${base_image}:${base_version}-jdk
    
    WORKDIR /oortfy
    
    COPY . .
    
    RUN javac Main.java
    
    EXPOSE ${port}
    
    CMD ["java", "Main"]
    ''',
    
    "golang":'''\
    FROM ${base_image}:${base_version}-alpine
    
    WORKDIR /oortfy
    
    COPY . .
    
    RUN go mod download
    
    CMD ["go", "run", "main.go"]
    ''',
    
    "dotnet":'''\
    FROM m${base_image}:${base_version}
    
    WORKDIR /oortfy
    
    COPY . .
    
    RUN dotnet restore
    
    EXPOSE 5000/tcp
    
    CMD ["dotnet", "run"]
    ''',
    
    "html":'''\
    FROM ${base_image}:${base_version}
    
    COPY ./public-html/ /usr/local/apache2/htdocs/
    ''',
    
    "php":'''\
    FROM ${base_image}:${base_version}-apache
    
    COPY . /var/www/html/
    
    EXPOSE 80
    
    CMD ["apache2-foreground"]
    '''}

    return template_dict