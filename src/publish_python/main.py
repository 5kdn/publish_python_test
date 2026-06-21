"""GUI アプリケーションのエントリポイントを提供する。"""

from publish_python.application_service import run_application


def main() -> None:
    """GUI アプリケーションを起動する。"""
    run_application()


if __name__ == "__main__":
    main()
