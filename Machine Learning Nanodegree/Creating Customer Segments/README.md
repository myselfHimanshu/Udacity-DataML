# Creating Customer Segments

Unsupervised Learning Project<br />
Most of the data one collects doesn’t necessarily fit into nice, labeled categories. Many times not only is data not labeled, but categories are unknown! In this project we will take unstructured data, and then attempt to understand the patterns and natural categories that the data fits into. First you’ll learn about methods that are useful for dealing with data without labels, then you’ll apply this to a dataset of your choice, learning what natural categories sit inside it.

## Template code

In this directory (`customer_segments/`), run `ipython notebook`, open `customer_segments.ipynb` and follow the instructions.

<b>Code Notebook :</b>  customer_segments.ipynb <br />
<b>Project Report Questions: </b> customer_segments.html

Note: You need Python 2.7, NumPy, pandas, matplotlib and scikit-learn to work on this notebook.

## Dataset

The dataset refers to clients of a wholesale distributor. It includes the annual spending in monetary units (m.u.) on diverse product categories.

It is part of a larger database published with the following paper:

Abreu, N. (2011). Analise do perfil do cliente Recheio e desenvolvimento de um sistema promocional. Mestrado em Marketing, ISCTE-IUL, Lisbon.

## Attributes

- Fresh: annual spending (m.u.) on fresh products (Continuous)
- Milk: annual spending (m.u.) on milk products (Continuous)
- Grocery: annual spending (m.u.)on grocery products (Continuous)
- Frozen: annual spending (m.u.)on frozen products (Continuous)
- Detergents_Paper: annual spending (m.u.) on detergents and paper products (Continuous)
- Delicatessen: annual spending (m.u.)on and delicatessen products (Continuous)

## Descriptive statistics

**Attribute: (Minimum, Maximum, Mean, Std. Deviation)**

- Fresh: ( 3, 112151, 12000.30, 12647.329)
- Milk: (55, 73498, 5796.27, 7380.377)
- Grocery: (3, 92780, 7951.28, 9503.163)
- Frozen: (25, 60869, 3071.93, 4854.673)
- Detergents_Paper: (3, 40827, 2881.49, 4767.854)
- Delicatessen: (3, 47943, 1524.87, 2820.106)
