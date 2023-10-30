# cellsize_detector


指定したディレクトリ内の複数の画像（.tif形式）から細胞のサイズを検出し、結果をCSVファイルとして保存します。

**コマンド引数**
--input または -i: 入力画像ファイルが保存されているディレクトリのパス（デフォルトは input ディレクトリ）。  
--output または -o: 結果を保存するディレクトリのパス（デフォルトは output ディレクトリ）。  
--width または -wi: 1ピクセルの幅（デフォルトは2.71）。  
--height または -he: 1ピクセルの高さ（デフォルトは2.86）。  

**スクリプトの実行方法**  
`python script.py --input /path/to/input/directory --output /path/to/output/directory --width 2.71 --height 2.86`


**注意事項**  
入力画像は .tif 形式。  
画像内の細胞は背景から十分に区別されている必要がある。  
