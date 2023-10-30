# cellsize_detector

Cell Size Detector
このプログラムは、指定したディレクトリ内の複数の画像（.tif形式）から細胞のサイズを検出し、結果をCSVファイルとして保存するツールです。

使用方法
プログラムはコマンドライン引数を使用して実行します。以下は引数の説明です：

--input または -i: 入力画像ファイルが保存されているディレクトリのパス（デフォルトは input ディレクトリ）。
--output または -o: 結果を保存するディレクトリのパス（デフォルトは output ディレクトリ）。
--width または -wi: 1ピクセルの幅（デフォルトは2.71）。
--height または -he: 1ピクセルの高さ（デフォルトは2.86）。

スクリプトの実行方法
python script.py --input /path/to/input/directory --output /path/to/output/directory --width 2.71 --height 2.86


注意事項
入力画像は .tif 形式である必要があります。
画像内の細胞は背景から十分に区別されている必要があります。不適切な画像では正確な結果が得られない可能性があります。