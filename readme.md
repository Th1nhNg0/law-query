Current support documents:

- Bộ luật dân sự 2015
- Bộ luật hình sự 2015
- Bộ luật lao động 2019
- Bộ luật hàng hải Việt Nam 2015
- Bộ luật tố tụng dân sự 2015
- Bộ luật tố tụng hình sự 2015

# Installation

```bash
git clone https://github.com/Th1nhNg0/law-query
cd law-query

python -m venv .env
source .env/bin/activate

# make sure you are using the latest pip
python -m pip install -U pip setuptools wheel

pip install --no-build-isolation --editable .
```

# Usage

```py
from lawquery import Engine, list_documents

# list of document paths
document_paths = list_documents()
print(document_paths)

# create engine
engine = Engine(filepath=document_paths[0])
# print info of document
print(engine)
# print outline tree
engine.print_tree()

# query
# node_type: root,phần,chương,mục,điều,khoản,điểm
# node_id: '1','2','I','II','nhất','hai','a','b'...
results = engine.query(node_type='điều', node_id='1')
results = engine.query( node_id='1')
results = engine.query( node_type='phần')
results = engine.query( name='hôn nhân')

# query by path: from parent to child
# param is list of dict, the parameter of engine.query function
results = engine.query_by_path([
    {
        'node_type': 'phần',
        'node_id': 'hai'
    },
    {
        'node_type': 'chương',
        'node_id': 'I'
    },
    {
        'node_type': 'mục',
        'node_id': '1'
    },
    {
        'node_type': 'điều',
        'node_id': '50'
    }
])

```
