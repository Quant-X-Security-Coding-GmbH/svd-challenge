# SVD Challenge

SVD Challenge is a pedagogical example which allows you to test limits and computation timings of the used processor. 
It belongs to the domain of quantum-ai and addresses anyone with interest in the math behind D-Wave coding.

Singular values of a matrix are a generalization of the notion of Eigenvalues.
With Eigenvalues we can quantify the expansion or compression of a linear transformation of a vector space.
The linear transformation of a vector space is represented by a
normal square matrix. 
So Eigenvalues can only be computed for normal square matrices.

Singular values on the other hand can be computed for any matrix, in other words for any linear map from a vector space 
with dimension *m* to another vector space with dimension *n*).
Singular Value Decomposition (SVD) is a useful tool for

* data reduction 
* dimensionality reduction

and can be efficiently  used as a foundation for machine learning.

We want to test the limits and timings of SVD on binary and D-Wave processors,
in particular for so-called sparse matrices (matrices with many zero entries).

![D-Wave Logo](dwave_logo.png)

## Challenges

* The size of a matrix (RAM limit)
* The density of a sparse matrix (algorithmic challenge)

Density refers to the percentage of non-zero entries in a matrix with many zeros.

_____________________________________________________________________________________

## Usage

You can run the SVD challenge by executing the following command in the terminal:

```bash
cd [path to your cloned svd_challenge repository]
python svd_challenge.py
```

If your example requires user input, make sure to specify any input limitations.

## Code Overview

A general overview of how the code works.

We prefer descriptions in bite-sized bullet points:

* Here's an example bullet point

## Code Specifics

Notable parts of the code implementation.

This is the place to:

* Highlight a part of the code implementation
* Talk about unusual or potentially difficult parts of the code
* Explain a code decision
* Explain how parameters were tuned

Note: there is no need to repeat everything that is already well-documented in
the code.

## References

A. Person, "Title of Amazing Information", [short link
name](https://example.com/)

## License

Released under the Apache License 2.0. See [LICENSE](LICENSE) file.
