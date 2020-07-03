# anat-from-MNI
This is a Python code to find the anatomical location of a MNI coordinate.

The original code is a matlab one from Xu Cui found [in his website][1]

[1]: https://alivelearn.net/?p=1456

The `TDdatabase.mat` is also found in Xu Cui's website

#### How to use it?

Let's find the structure of two points in MNI coordinates (58,-29,19) and (30,9,12):

```python
     mni=[[58,-29,19],[30,9,12]]
     [one_line,table]=find_structure(mni)
```

We see the results
```python
    >>> one_line[0]
    ' // Right Cerebrum // Parietal Lobe // Postcentral Gyrus // Gray Matter // brodmann area 40 // Temporal_Sup_R (aal)'
    >>> one_line[1]
    ' // Right Cerebrum // Sub-lobar // Extra-Nuclear // White Matter // undefined // undefined'
    >>> table
    [['Right Cerebrum',
  'Parietal Lobe',
  'Postcentral Gyrus',
  'Gray Matter',
  'brodmann area 40',
  'Temporal_Sup_R (aal)'],
 ['Right Cerebrum',
  'Sub-lobar',
  'Extra-Nuclear',
  'White Matter',
  'undefined',
  'undefined']]
```

