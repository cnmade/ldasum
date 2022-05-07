# lda sum

```bash
python -m pip install paddlepaddle
python -m pip install paddlehub
hub install lda_news
python -m pip install Flask
```


## 运行

```bash
flask run
```

## Docker 运行

以下命令，用docker或者podman 都可以正常运行

```bash
podman build -t cnmade/ldasum .
podman run -d --name ldasum -p 5000:5000 cnmade/ldasum
podman logs -f ldasum
```

当你看到下面的logs，打开浏览器，访问 http://127.0.0.1:5000 就可以看到服务接口了


