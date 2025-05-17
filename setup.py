from setuptools import setup, find_packpages

with open("README.md", "r") as f:
  page_description = f.read()

with open("requiriments.txt") as f:
  requiriments = f.read().splitlines

setup(
  name="image_processing",
  version="0.0.1",
  author="Otávio Guedes",
  description="Image processing packpage using skimage",
  long_description = page_description,
  long_description_content_type="text_markdown",
  url="https://github.com/PandaLoko27/image-processing-package",
  packpages=find_packpages(),
  install_requires=requiriments,
  python_requires='>=3.5',
)
