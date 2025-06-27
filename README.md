# Binary Search Algorithm 

This mini project demonstrates iterative and recursive Binary Search Algorithms.    
Showing two classic divide and conquer implementations of binary search:<br><br>

<small>

| File          | Method        | Purpose                                         |
| ------------- | ------------- |-------------------------------------------------|
| `bin-iter.py` | **Iterative** | Loops until the target is found                 |
| `bin-rec.py`  | **Recursive** | Calls itself on ever smaller slices of the list |


Binary search efficiently halves the search space at every step, giving O(log n) time complexity.<br>
It enables database queries, drives search engine indexing, and supports real time apps.<br><br>

</small>

---

<small>

### Quick Start  
**Clone this repo:**       
```git clone git@github.com:neilburbage/Python-Bin-Search-Algor```  
**Make sure you've added your SSH key first:**     
```https://docs.github.com/en/authentication/connecting-to-github-with-ssh```  
```$ cd Python-Bin-Search-Algor```  
**Create a virtual environment:**     
```python -m venv .venv```  
```# Linux / macOS: source .venv/bin/activate```     
```# Windows (PowerShell): .venv\Scripts\activate```  
```# Windows (cmd): .venv\Scripts\activate.bat```  
**Run the Binary Search algorithms:**  
```bin-iter.py # iterative demo```  
```bin-rec.py # recursive demo```

</small>

---

### Project Layout

<small>

```
├── bin-iter.py # runs the iterative algorithm
├── bin-rec.py  # runs the recursive algorithm
├── .gitignore         # venv/, __pycache__/
└── README.md          # you are here
```

</small>

---