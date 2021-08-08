# SVD Challenge

## Possible benchmark matrices

We could use sparse matrices as to be generated according to this paper by S. Rump:
https://www.tuhh.de/ti3/paper/rump/NiRuOi11.pdf

One method described is the generation of ill-conditioned matrices similar to the following
companion matrix: Let A be an nxn integer matrix of the following form :


           a1  a2  a3  a4  ...  a(n-1)  a(n)
           
           1  -l1  0   0   ...    0      0
           
           0   1  -l2  0   ...    0      0
             
           0   0    1 -l3  ...    0      0
           
           ...  ...   ...  ...    ...   ...
           
           0   0    0   0  ...    1     -l(n-1)



The entries a_i  and  l_i  are defined based on the Pell equation, well known in algebraic number theory,
according to a recursive scheme which is easy to code in any language allowing for recursive programming.
The resulting matrices have very large condition numbers, and a specific pattern of the singular values.

_____________________________________________________________________________________




Describe your example and specify what it is demonstrating. Consider the
following questions:

* Is it pedagogical or a usable application?
* Does it belong to a particular domain such as material simulation or logistics? 
* What level of Ocean proficiency does it target (beginner, advanced, pro)? 

A clear description allows us to properly categorize your example.

Images are encouraged. If your example produces a visualization, consider
displaying it here.

![D-Wave Logo](dwave_logo.png)

## Usage

A simple command that runs your program. For example,

```bash
python <demo_name>.py
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
