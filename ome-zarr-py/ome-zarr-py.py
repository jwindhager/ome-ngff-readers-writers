# https://ome-zarr.readthedocs.io/en/stable/
# https://ome-zarr.readthedocs.io/en/stable/python.html#reading-ome-ngff-images
# https://ome-zarr.readthedocs.io/en/stable/api/writer.html#ome_zarr.writer.write_image

import matplotlib.pyplot as plt
from ome_zarr import writer
from ome_zarr.io import parse_url
from ome_zarr.reader import Reader
import zarr


def show_image(image):
    plt.imshow(image)
    plt.show()


def read_test(input):
    # read the image data
    reader = Reader(parse_url(input))
    # nodes may include images, labels etc
    nodes = list(reader())
    # first node will be the image pixel data
    image_node = nodes[0]
    metadata = image_node.metadata
    print(metadata)
    image_data = image_node.data[0]  # resolution level 0
    print(image_data.shape)
    show_image(image_data[0, 0, 0, ...])
    return image_data


def write_test(output, image_data):
    # %%
    group = zarr.open_group(output, mode='w')
    result = writer.write_image(image=image_data,
                                group=group,
                                storage_options={'dimension_separator': '/'})
    print(result)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input = "https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0101A/13457539.zarr"
    output = "C:/Project/slides/test.ome.zarr"
    image_data = read_test(input)
    write_test(output, image_data)
