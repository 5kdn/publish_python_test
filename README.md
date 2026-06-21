# Tkinter によるシンプルな GUI アプリ

画面に `Hello World` を表示するだけのシンプルな Python 製 GUI アプリである。

## 開発実行

```powershell
uv run hello-gui
```

## Windows 向け exe ビルド

`PyInstaller` を使って単一ファイルの GUI 実行ファイルを生成する。

```powershell
./scripts/build_exe.ps1
```

生成物は `dist/publish-python.exe` である。

ビルド時の要点は次のとおりである。

- `python -m pip install ".[build]"` でビルド依存を導入する。
- `python -m PyInstaller` で `.spec` を解釈してビルドする。
- `--onefile` 相当で単一ファイル化する。
- `console=False` によりコンソールを表示しない GUI アプリとして扱う。
- `.spec` ファイルは [packaging/publish_python.spec](/D:/Projects/labs/publish-python/packaging/publish_python.spec) に分離し、ビルド設定責務をアプリ本体から切り離す。

## リリース自動化

`main` ブランチへの push を契機に [release-please workflow](/D:/Projects/labs/publish-python/.github/workflows/release-please.yml) が動作し、Conventional Commits に基づく Release PR と GitHub Release を管理する。

設定は [.release-please-config.json](/D:/Projects/labs/publish-python/.release-please-config.json) と [.release-please-manifest.json](/D:/Projects/labs/publish-python/.release-please-manifest.json) に分離している。

workflow は `secrets.RELEASE_PLEASE_PAT` を使用する。

GitHub Release が実際に作成された場合のみ、Windows runner 上で `./scripts/build_exe.ps1` を実行して `dist/publish-python.exe` を生成し、そのまま release asset として添付する。
