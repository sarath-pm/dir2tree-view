# dir2tree-view
The Python package <b>*dir2tree-view*</b> contains a straightforward module to print or generate a clutter - free directory tree view with icons.

## Requirements

```
python >= 3.0
```

## Installation
```
pip install dir2tree-view
```

## Usage
> Pass the directory path to the generate method

```python
from TreeView import Tree
op = Tree()
op.create(r'directory_path')
```

> Output

```
🖿  Test/
   🖿  Test1/
       ➥  test1.txt - Copy.txt   
       ➥  test1.txt.txt
   🖿  Test2/
       ➥  test.bmp
       ➥  test1.bmp
      🖿  New folder/
          ➥  New DOC Document.doc
   🖿  Test3/
       ➥  New Rich Text Document.rtf
       ➥  New XLS Worksheet.xls
      🖿  New folder/
          ➥  New PPTX Presentation.pptx
```

## License
This project is licensed under the MIT License

## Author 
[Sarath P M](sarath.pm.github.io)