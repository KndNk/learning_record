FROM python:3.10.9-slim-buster

WORKDIR /python-app
RUN pip3 install flask

COPY ./app.py /python-app/app.py

EXPOSE 8080
ENTRYPOINT ["python3", "app.py"]

#`FROM`は、ベースとなるコンテナイメージを指定。
# `WORKDIR`は、コンテナの作業ディレクトリを指定。
# `RUN`は、「docker image build」コマンドでイメージを構築するときにコンテナ内でシェルコマンドを実行します。
#           今回はFlaskをインストールするためのpip（Pytyhonのパッケージ管理システム）のコマンド「pip install Flask」を実行する指定になっています。
# `COPY`は、「docker image build」コマンドでイメージを構築するときに、ローカル環境からコンテナ内にファイルをコピーして設置するための指定です。
#           「COPY」の1つ目にはコピー元のホスト（ローカル環境）ディレクトリ、2つ目にはコピー先のコンテナのディレクトリを指定します。
# `EXPSE`は、コンテナのポートを公開するコマンド。
# `ENTRYPOINT`は、コンテナを 実行ファイル(executable) として処理するように設定。