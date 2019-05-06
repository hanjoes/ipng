from ipng import PNG


def test_metadata():
    png = PNG(file='tests/data/mario.png')
    metadata = png.metadata
    assert '''\
basic spec:         width:360,height:490,bit_depth:8,color_type:6,pixel_size(bit):32,compression:0,filter:0,interlace:0
chunk histogram:    IHDR:1,IDAT:1,IEND:1
compression spec:   method/flag:120,additional:1,check:35\
''' == metadata


def test_same():
    png = PNG(file='tests/data/mario.png')
    png.render(output='/tmp/ipng_test_same.png')

    png_tmp = PNG(file='/tmp/ipng_test_same.png')
    assert png_tmp.bitmap == png.bitmap
