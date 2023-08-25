import pytest
import os
from itertools import combinations
from PIL import Image
from src.image_format_converter.converter import ALLOWED_FORMATS, convert_images_in_directory

# All allowed format combinations
all_pairs = [(a, b) for a, b in combinations(ALLOWED_FORMATS, 2)]  # unique combinations
all_pairs += [(b, a) for a, b in all_pairs]  # reversed pairs

# path to the baseline folder
TEST_DIR = "test_resources"
OUTPUT_DIR = "test_resources/test_output"


def test_preserve_image_dimensions():
    input_file = os.path.join(TEST_DIR, "sample.png")
    original = Image.open(input_file)

    convert_images_in_directory(TEST_DIR, "png", "jpg", OUTPUT_DIR)

    output_file = os.path.join(OUTPUT_DIR, "sample.jpg")
    converted = Image.open(output_file)

    assert original.size == converted.size


def test_recursivity():
    convert_images_in_directory(TEST_DIR, "png", "jpg", recursive=True)

    assert os.path.exists(os.path.join(TEST_DIR, "subfolder/sample.jpg"))
    assert os.path.exists(os.path.join(TEST_DIR, "subfolder/subfolder2/sample.jpg"))
    assert os.path.exists(os.path.join(TEST_DIR, "subfolder/subfolder2/subfolder3/sample.jpg"))


def test_overwrite():
    convert_images_in_directory(TEST_DIR, "png", "jpg", OUTPUT_DIR, overwrite=True)

    # original png should not exist, but jpg version should
    assert not os.path.exists(os.path.join(TEST_DIR, "sample.png"))
    assert os.path.exists(os.path.join(TEST_DIR, "sample.jpg"))


def test_output_directory_set():
    convert_images_in_directory(TEST_DIR, "png", "jpg", OUTPUT_DIR)

    assert os.path.exists(os.path.join(OUTPUT_DIR, "sample.jpg"))


def test_output_directory_not_set():
    convert_images_in_directory(TEST_DIR, "png", "jpg")

    assert os.path.exists(os.path.join(TEST_DIR, "sample.jpg"))


@pytest.mark.parametrize("input_format,output_format", all_pairs)
def test_conversion_for_all_allowed_pairs(input_format, output_format):
    convert_images_in_directory(TEST_DIR, input_format, output_format, OUTPUT_DIR)

    # Check if the output format exists in the output directory
    assert os.path.exists(os.path.join(OUTPUT_DIR, f"sample.{output_format}"))
