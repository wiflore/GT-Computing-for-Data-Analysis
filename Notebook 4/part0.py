
# coding: utf-8

# # Part 0: Representing numbers as strings
# 
# The following exercises are designed to reinforce your understanding of how we can view the encoding of a number as string of digits in a given base.
# 
# > If you are interested in exploring this topic in more depth, see the ["Floating-Point Arithmetic" section](https://docs.python.org/3/tutorial/floatingpoint.html) of the Python documentation.

# ## Integers as strings
# 
# Consider the string of digits:
# 
# ```python
#     '16180339887'
# ```
# 
# If you are told this string is for a decimal number, meaning the base of its digits is ten (10), then its value is given by
# 
# $$
#     [\![ \mathtt{16180339887} ]\!]_{10} = (1 \times 10^{10}) + (6 \times 10^9) + (1 \times 10^8) + \cdots + (8 \times 10^1) + (7 \times 10^0) = 16,\!180,\!339,\!887.
# $$
# 
# Similarly, consider the following string of digits:
# 
# ```python
#     '100111010'
# ```
# 
# If you are told this string is for a binary number, meaning its base is two (2), then its value is
# 
# $$
#     [\![ \mathtt{100111010} ]\!]_2 = (1 \times 2^9) + (1 \times 2^6) + \cdots + (1 \times 2^1).
# $$
# 
# (What is this value?)
# 
# And in general, the value of a string of $d+1$ digits in base $b$ is,
# 
# $$
#   [\![ s_d s_{d-1} \cdots s_1 s_0 ]\!]_b = \sum_{i=0}^{d} s_i \times b^i.
# $$

# **Bases greater than ten (10).** Observe that when the base at most ten, the digits are the usual decimal digits, `0`, `1`, `2`, ..., `9`. What happens when the base is greater than ten? For this notebook, suppose we are interested in bases that are at most 36; then, we will adopt the convention of using lowercase Roman letters, `a`, `b`, `c`, ..., `z` for "digits" whose values correspond to 10, 11, 12, ..., 35.
# 
# > Before moving on to that exercise, run the following code cell. It has three functions, which are used in some of the testing code. Given a base, one checks whether a single-character input string is a valid digit; and the other returns a list of all valid string digits. (The third one simply prints the valid digit list, given a base.) If you want some additional practice reading code, you might inspect these functions.

# In[1]:


def is_valid_strdigit(c, base=2):
    if type (c) is not str: return False # Reject non-string digits
    if (type (base) is not int) or (base < 2) or (base > 36): return False # Reject non-integer bases outside 2-36
    if base < 2 or base > 36: return False # Reject bases outside 2-36
    if len (c) != 1: return False # Reject anything that is not a single character
    if '0' <= c <= str (min (base-1, 9)): return True # Numerical digits for bases up to 10
    if base > 10 and 0 <= ord (c) - ord ('a') < base-10: return True # Letter digits for bases > 10
    return False # Reject everything else

def valid_strdigits(base=2):
    POSSIBLE_DIGITS = '0123456789abcdefghijklmnopqrstuvwxyz'
    return [c for c in POSSIBLE_DIGITS if is_valid_strdigit(c, base)]

def print_valid_strdigits(base=2):
    valid_list = valid_strdigits(base)
    if not valid_list:
        msg = '(none)'
    else:
        msg = ', '.join([c for c in valid_list])
    print('The valid base ' + str(base) + ' digits: ' + msg)
    
# Quick demo:
print_valid_strdigits(6)
print_valid_strdigits(16)
print_valid_strdigits(2)


# **Exercise 0** (1 point). Write a function, `eval_strint(s, base)`, which given a string of digits `s` and a base `base`, returns its value as an integer.
# 
# That is, this function essentially implements the mathematical object, $[\![ s ]\!]_b$, which would convert a string $s$ to its numerical value, assuming its digits are given in base $b$. For example:
# 
# ```python
#     eval_strint('100111010', base=2) == 314
# ```
# 
# > Hint: Python makes this exercise very easy. Search Python's online documentation for information about the `int()` constructor to see how you can apply it to solve this problem. (You have encountered this constructor already, in Lab/Notebook 2.)

# In[2]:


def eval_strint(s, base):
    
    return int(s, base)

eval_strint('100111010', base=2)


# In[3]:


# Test: `eval_strint_test`

def check_eval_strint(s, v, base=2):
    v_s = eval_strint(s, base)
    msg = "'{}' -> {}".format (s, v_s)
    print(msg)
    assert v_s == v, "Results do not match expected solution."

# Test 0: From the videos
check_eval_strint('16180339887', 16180339887, base=10)

# Test 1: Also from the videos
check_eval_strint('100111010', 314, base=2)

# Test 2
check_eval_strint('a205b064', 2718281828, base=16)

print ("\n(Passed!)")


# ## Fractional values
# 
# Recall that we can extend the basic string representation to include a fractional part by interpreting digits to the right of the "fractional point" (i.e., "the dot") as having negative indices. For instance,
# 
# $$
#     [\![ \mathtt{3.14} ]\!]_{10} = (3 \times 10^0) + (1 \times 10^{-1}) + (4 \times 10^{-2}).
# $$
# 
# Or, in general,
# 
# $$
#   [\![ s_d s_{d-1} \cdots s_1 s_0 \, \underset{\Large\uparrow}{\Huge\mathtt{.}} \, s_{-1} s_{-2} \cdots s_{-r} ]\!]_b = \sum_{i=-r}^{d} s_i \times b^i.
# $$

# **Exercise 1** (3 points). Suppose a string of digits `s` in base `base` contains up to one fractional point. Complete the function, `eval_strfrac(s, base)`, so that it returns its corresponding floating-point value. Your function should *always* return a value of type `float`, even if the input happens to correspond to an exact integer.
# 
# Examples:
# 
# ```python
#     eval_strfrac('3.14', base=10) ~= 3.14
#     eval_strfrac('100.101', base=2) == 4.625
# ```
# 
# > Because of potential floating-point roundoff errors, as explained in the videos, conversions based on the general polynomial formula given previously will not be exact. The testing code will include a built-in tolerance to account for such errors.

# In[4]:


def eval_strfrac(s, base):
    l = []
    l = '0123456789abcdefghijklmnopqrstuvwxyz'
    s2i = {}
    for i, k in enumerate(l):
        s2i[k] = i

    ret = 0
    if "." not in s: bef = s
    else: bef, aft = s.split(".")
    for i in enumerate(reversed(bef)):
        integer = float(s2i[i[1]])
        if integer >= base: raise ValueError
        ret += base**i[0] * integer
    if "." not in s: return ret
    for i in enumerate(aft):
        integer = s2i[i[1]]
        if integer >= base: raise ValueError
        ret += base**-(i[0] + 1) * integer
    return (ret) 

print(eval_strfrac('1.2500', base=10))


# In[5]:


# Test: `eval_strfrac_test`

def check_eval_strfrac(s, v_true, base=2, tol=1e-7):
    v_you = eval_strfrac(s, base)
    assert type(v_you) is float, "Your function did not return a `float` as instructed."
    delta_v = v_you - v_true
    msg = "[{}]_{{{}}} ~= {}: You computed {}, which differs by {}.".format(s, base, v_true,
                                                                            v_you, delta_v)
    print(msg)
    assert abs(delta_v) <= tol, "Difference exceeds expected tolerance."
    
# Test cases from the video
check_eval_strfrac('3.14', 3.14, base=10)
check_eval_strfrac('100.101', 4.625, base=2)
check_eval_strfrac('11.0010001111', 3.1396484375, base=2)

# A hex test case
check_eval_strfrac('f.a', 15.625, base=16)

# Random test cases
def check_random_strfrac():
    from random import randint
    b = randint(2, 36) # base
    d = randint(0, 5) # leading digits
    r = randint(0, 5) # trailing digits
    v_true = 0.0
    s = ''
    possible_digits = valid_strdigits(b)
    for i in range(-r, d+1):
        v_i = randint(0, b-1)
        s_i = possible_digits[v_i]

        v_true += v_i * (b**i)
        s = s_i + s
        if i == -1:
            s = '.' + s
    check_eval_strfrac(s, v_true, base=b)
    
for _ in range(10):
    check_random_strfrac()

print("\n(Passed!)")


# ## Floating-point encodings
# 
# Recall that a floating-point encoding or format is a normalized scientific notation consisting of a _base_, a _sign_, a fractional _significand_ or _mantissa_, and a signed integer _exponent_. Conceptually, think of it as a tuple of the form, $(\pm, [\![s]\!]_b, x)$, where $b$ is the digit base (e.g., decimal, binary); $\pm$ is the sign bit; $s$ is the significand encoded as a base $b$ string; and $x$ is the exponent. For simplicity, let's assume that only the significand $s$ is encoded in base $b$ and treat $x$ as an integer value. Mathematically, the value of this tuple is $\pm \, [\![s]\!]_b \times b^x$.

# **IEEE double-precision.** For instance, Python, R, and MATLAB, by default, store their floating-point values in a standard tuple representation known as _IEEE double-precision format_. It's a 64-bit binary encoding having the following components:
# 
# - The most significant bit indicates the sign of the value.
# - The significand is a 53-bit string with an _implicit_ leading one. That is, if the bit string representation of $s$ is $s_0 . s_1 s_2 \cdots s_d$, then $s_0=1$ always and is never stored explicitly. That also means $d=52$.
# - The exponent is an 11-bit string and is treated as a signed integer in the range $[-1022, 1023]$.
# 
# Thus, the smallest positive value in this format $2^{-1022} \approx 2.23 \times 10^{-308}$, and the smallest positive value greater than 1 is $1 + \epsilon$, where $\epsilon=2^{-52} \approx 2.22 \times 10^{-16}$ is known as _machine epsilon_ (in this case, for double-precision).

# **Special values.** You might have noticed that the exponent is slightly asymmetric. Part of the reason is that the IEEE floating-point encoding can also represent several kinds of special values, such as infinities and an odd bird called "not-a-number" or `NaN`. This latter value, which you may have seen if you have used any standard statistical packages, can be used to encode certain kinds of floating-point exceptions that result when, for instance, you try to divide zero by zero.
# 
# > If you are familiar with languages like C, C++, or Java, then IEEE double-precision format is the same as the `double` primitive type. The other common format is single-precision, which is `float` in those same languages.

# **Inspecting a floating-point number in Python.** Python provides support for looking at floating-point values directly! Given any floating-point variable, `v` (that is, `type(v) is float`), the method `v.hex()` returns a string representation of its encoding. It's easiest to see by example, so run the following code cell:

# In[6]:


def print_fp_hex(v):
    assert type(v) is float
    print("v = {} ==> v.hex() == '{}'".format(v, v.hex()))
    
print_fp_hex(0.0)
print_fp_hex(1.0)
print_fp_hex(16.0625)
print_fp_hex(-0.1)


# Observe that the format has these properties:
# * If `v` is negative, the first character of the string is `'-'`.
# * The next two characters are always `'0x'`.
# * Following that, the next characters up to but excluding the character `'p'` is a fractional string of hexadecimal (base-16) digits. In other words, this substring corresponds to the significand encoded in base-16.
# * The `'p'` character separates the significand from the exponent. The exponent follows, as a signed integer (`'+'` or `'-'` prefix). Its implied base is two (2)---**not** base-16, even though the significand is.
# 
# Thus, to convert this string back into the floating-point value, you could do the following:
# * Record the sign as a value, `v_sign`, which is either +1 or -1.
# * Convert the significand into a fractional value, `v_signif`, assuming base-16 digits.
# * Extract the exponent as a signed integer value, `v_exp`.
# * Compute the final value as `v_sign * v_signif * (2.0**v_exp)`.
# 
# For example, here is how you can get 16.025 back from its `hex()` representation, `'0x1.0100000000000p+4'`:

# In[7]:


#Recall: v = 16.0625 ==> v.hex() == '0x1.0100000000000p+4'
print((+1.0) * eval_strfrac('1.0100000000000', base=16) * (2**4))


# **Exercise 2** (5 points). Write a function, `fp_bin(v)`, that determines the IEEE-754 tuple representation of any double-precision floating-point value, `v`. That is, given the variable `v` such that `type(v) is float`, it should return a tuple with three components, `(s_sign, s_bin, v_exp)` such that
# 
# * `s_sign` is a string representing the sign bit, encoded as either a `'+'` or `'-'` character;
# * `s_signif` is the significand, which should be a string of 54 bits having the form, `x.xxx...x`, where there are (at most) 53 `x` bits (0 or 1 values);
# * `v_exp` is the value of the exponent and should be an _integer_.
# 
# For example:
# 
# ```python
#     v = -1280.03125
#     assert v.hex() == '-0x1.4002000000000p+10'
#     assert fp_bin(v) == ('-', '1.0100000000000010000000000000000000000000000000000000', 10)
# ```
# 
# > There are many ways to approach this problem. One we came up used an idea in this Stackoverflow post: https://stackoverflow.com/questions/1425493/convert-hex-to-binary

# In[8]:


def fp_bin(num):
    num = float(num)
    exponent=0
    shifted_num = num
    while shifted_num != int(shifted_num):        
        shifted_num*=2
        exponent += 1
    binary='{0:0{1}b}'.format(int(shifted_num), exponent + 1)
    integer_part=binary[:-exponent]
    
    sign = '+'
    if binary[0] == '-':
        sign = '-'
        binary = binary[1:]
        integer_part = integer_part[1:]
    
    len_int = len(integer_part) - 1
    sum_binary = 0
    for item in binary:
        sum_binary += int(item)
    
    for item in binary:
        if item is '0':
            len_int -= 1
            binary = binary[1:]
        else:
            break
            
    if sum_binary is 0:
        len_int = 0
            
    if len(binary) < 53:
        binary += '0'*(53-len(binary))
        
    binary = binary[0] + '.' + binary[1:]
    
    return (sign, binary, len_int)

    

print(fp_bin('0.0'))  
print(fp_bin('-1280.03125'))
print(fp_bin('6.2831853072'))
print(fp_bin('-0.1')) 
print(fp_bin(1.0 + (2 ** (-52)))) 
  
# 110.1



# In[9]:


# Test: `fp_bin_test`

def check_fp_bin(v, x_true):
    x_you = fp_bin(v)
    print("""{} [{}] ==
         {}
vs. you: {}
""".format(v, v.hex(), x_true, x_you))
    assert x_you == x_true, "Results do not match!"
    
check_fp_bin(0.0, ('+', '0.0000000000000000000000000000000000000000000000000000', 0))
check_fp_bin(-1280.03125, ('-', '1.0100000000000010000000000000000000000000000000000000', 10))
check_fp_bin(6.2831853072, ('+', '1.1001001000011111101101010100010001001000011011100000', 2))
check_fp_bin(-0.1, ('-', '1.1001100110011001100110011001100110011001100110011010', -4))
check_fp_bin(1.0 + (2**(-52)), ('+', '1.0000000000000000000000000000000000000000000000000001', 0))
print("\n(Passed!)")


# **Exercise 3** (3 points). Suppose you are given a floating-point value in a base given by `base` and in the form of the tuple, `(sign, significand, exponent)`, where
# 
# * `sign` is either the character '+' if the value is positive and '-' otherwise;
# * `significand` is a _string_ representation in base-`base`;
# * `exponent` is an _integer_ representing the exponent value.
# 
# Complete the function,
# 
# ```python
# def eval_fp(sign, significand, exponent, base):
#     ...
# ```
# 
# so that it converts the tuple into a numerical value (of type `float`) and returns it.

# In[10]:


def eval_fp(sign, significand, exponent, base):
    if '.' in significand and exponent != 0:
        significand = significand.replace(".", "")
    if exponent > 0:
        significand = significand[0:exponent+1] + "." + significand[exponent+1:]
    elif exponent < 0 :
        significand  = "0" + "." + "0" * (abs(exponent)-1) + significand[0:]
    num = eval_strfrac(significand, base)
    return float((sign + str(num)))


# In[11]:


# Test: `eval_fp_test`

def check_eval_fp(sign, significand, exponent, v_true, base=2, tol=1e-7):
    v_you = eval_fp(sign, significand, exponent, base)
    delta_v = v_you - v_true
    msg = "('{}', ['{}']_{{{}}}, {}) ~= {}: You computed {}, which differs by {}.".format(sign, significand, base, exponent, v_true, v_you, delta_v)
    print(msg)
    assert abs(delta_v) <= tol, "Difference exceeds expected tolerance."
    
# Test 0: From the videos
check_eval_fp('+', '1.25000', -1, 0.125, base=10)

# Test 1: Random floating-point binary values
def gen_rand_fp_bin():
    from random import random, randint
    v_sign = 1.0 if (random() < 0.5) else -1.0
    v_mag = random() * (10**randint(-5, 5))
    v = v_sign * v_mag
    s_sign, s_bin, s_exp = fp_bin(v)
    return v, s_sign, s_bin, s_exp

for _ in range(5):
    (v_true, sign, significand, exponent) = gen_rand_fp_bin()
    check_eval_fp(sign, significand, exponent, v_true, base=2)


# **Exercise 4** (2 points). Suppose you are given two binary floating-point values, `u` and `v`, in the tuple form given above. That is, `u == (u_sign, u_signif, u_exp)` and `v == (v_sign, v_signif, v_exp)`, where the base for both `u` and `v` is two (2). Complete the function `add_fp_bin(u, v, signif_bits)`, so that it returns the sum of these two values with the resulting significand _truncated_ to `signif_bits` digits.
# 
# > _Note 0_: Assume that `signif_bits` _includes_ the leading 1. For instance, suppose `signif_bits == 4`. Then the significand will have the form, `1.xxx`.
# >
# > _Note 1_: You may assume that `u_signif` and `v_signif` use `signif_bits` bits (including the leading `1`). Furthermore, you may assume each uses far fewer bits than the underlying native floating-point type (`float`) does, so that you can use native floating-point to compute intermediate values.
# >
# > _Hint_: The test cell above defines a function, `fp_bin(v)`, which you can use to convert a Python native floating-point value (i.e., `type(v) is float`) into a binary tuple representation.

# In[12]:


def add_fp_bin(u, v, signif_bits):
    sign, bin_num, exponent = u
    u_float = eval_fp(sign, bin_num, exponent, base = 2)
    sign, bin_num, exponent = v
    v_float = eval_fp(sign, bin_num, exponent, base = 2)
    sign, bin_num, exponent = fp_bin((u_float + v_float))
    return (sign, bin_num[0:signif_bits+1], exponent)


# In[13]:


# Test: `add_fp_bin_test`

def check_add_fp_bin(u, v, signif_bits, w_true):
    w_you = add_fp_bin(u, v, signif_bits)
    msg = "{} + {} == {}: You produced {}.".format(u, v, w_true, w_you)
    print(msg)
    assert w_you == w_true, "Results do not match."

u = ('+', '1.010010', 0)
v = ('-', '1.000000', -2)
w_true = ('+', '1.000010', 0)
check_add_fp_bin(u, v, 7, w_true)

u = ('+', '1.00000', 0)
v = ('+', '1.00000', -5)
w_true = ('+', '1.00001', 0)
check_add_fp_bin(u, v, 6, w_true)

u = ('+', '1.00000', 0)
v = ('-', '1.00000', -5)
w_true = ('+', '1.11110', -1)
check_add_fp_bin(u, v, 6, w_true)

u = ('+', '1.00000', 0)
v = ('+', '1.00000', -6)
w_true = ('+', '1.00000', 0)
check_add_fp_bin(u, v, 6, w_true)

u = ('+', '1.00000', 0)
v = ('-', '1.00000', -6)
w_true = ('+', '1.11111', -1)
check_add_fp_bin(u, v, 6, w_true)

print("\n(Passed!)")


# **Done!** You've reached the end of `part0`. Be sure to save and submit your work. Once you are satisfied, move on to `part1`.
