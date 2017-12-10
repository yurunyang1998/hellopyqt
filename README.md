# process_video


这个仓库是用来处理一些视频，生成标记区域的图片或者xml文件的，有两个分支，代表两个功能

branch master： 这个分支是用来给通过视频生成标记区域的，鼠标圈定的范围就是要截取的区域

branch 2.0 : 这个分支是用来处理视屏，生成xml文件和当前视频所在的frame的，生成的xml文件是coco格式的。


先用xml_to_csv 生成xml和xml所对应的图片的 csv文件。
csv文件格式有些不整齐，用 filename ass_jpg.py 处理一下文件，再用excel处理一下 classes那一列，把多余的空格换行都去掉。

然后用genrate_tfrecord.py  将图片和csv 处理成record格式的数据集。
