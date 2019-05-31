server {
        listen       80;
        server_name  {{SERVER_NAME}};
        root         {{ROOT}};
        index index.html index.htm index.php;

        access_log  {{ACCESS_LOG}}  main;

        location /{
            try_files $uri $uri/ /index.php?$query_string;
        }


        location ~ \.php$ {
            fastcgi_pass   unix:/var/run/php-fpm/php-fpm.sock;
            fastcgi_index  index.php;
            fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
            include        fastcgi_params;
        }

    }