　
以下の参考ページをもとに構築する。
　参考ページ：https://zenn.dev/schnell/articles/56a1f6bed65688


コマンドメモ：
　〇Dockerのインストール
    `sudo yum update -y`　→ yumのパッケージをアップデートするコマンド。
    `sudo yum -y install docker` → dockerをインストールするコマンド。

　　※sudoは、スーパーユーザとしてコマンドを実行する際に使う。
　　※yumは、パッケージ管理システムであり、便利機能のコマンド。
　　※-yオプションは問い合わせにすべて"y"と答える。


　〇Dockerデーモンを起動
    `sudo systemctl start docker` → dockerサービスを起動するコマンド。
    `sudo systemctl enable docker` → dockerサービスの自動起動を有効かするコマンド。

　　※Dockerデーモンとは、コンテナを管理するために常駐するプロセス。
　　※systemctlは、サービスを管理するコマンド。サービスの起動、停止等が行える。
　　

　〇sudo無しでdockerコマンドを利用できるように(ec2-userはAmzon Linuxのデフォルトユーザー)
    `sudo usermod -aG docker ec2-user` → ec2-userを、dockerグループに追加するコマンド。
    　　　　　　　　　　　　　　　　　　　　 これにより、ec2-usrはdockerコマンドを実行可能となる。

　　※usermodは、ユーザアカウント情報を変更するコマンド。
　　※-aGオプションは、ユーザーを特定のグループに追加するためのものです。

　〇dockerコマンドが使えることを確認
    `docker info`

　〇docker hubにログイン
    `docker login`

　〇dockerイメージのビルド
    `docker build --tag dockerdemo ./`　→ 　カレントディレクトリのDockerfileを使用して、dockerdemoという名前のDockerイメージをビルドするコマンド。

    ※docker build は、Dockerイメージをビルドするコマンド。
    ※--tagは、ビルドされるDockerイメージにタグ付けするためのオプション。
    ※./は、ビルドするコンテキストを示すディレクトリ。

　〇コンテナ起動
    `docker run -d --name dockerdemo -e name='schnell' -p 80:8080 dockerdemo` →Dockerコンテナを実行するためのコマンド。

    ※docker run は、Dockerコンテナを実行するためのコマンド。
    ※-dは、デタッチモード(バックグランド)で実行するためのオプション。
    ※--name dockerdemoは、実行されるコンテナにdockerdemoという名前をつけるオプション。
    ※-e name = 'schnell'は、 実行中のコンテナに環境変数'name'を設定するためのオプション。
    ※-p 80:8080 は、コンテナのポートとホストのポートをマッピングするためのオプション。
    ※dockerdemoは、実行するDockerイメージの名前。


〇その他コマンド
　`docker stop ***`  →  ***(コンテナ名)を停止するコマンド。

　`docker ps -a`  →  コンテナリストを表示するコマンド。オプション-aをつけると、停止しているコンテナも取得できる。
