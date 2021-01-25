# textToHandwritten

## Install PILLOW Library first using either of following two:

```bash
pip install Pillow
```
If you have Pythons installed and want to install this for Python3:
```bash
python3 -m pip install Pillow
```

## Procedure to use 
1. Put the content you want to be handwritten in MyText file.

2. Follow formating  rule as given below to format Output.(check MyText file as well)

    a. Use `#` to switch to the new line
    
    b. Use `^^` to align the text to centre(Applies to the whole line)
    
    c. Use `->` for Tab(You can't use multiple spaces as this is whitespace collapsing)

3. Run the `maincode.py`

4. Output will be generated in `final` directory with name done1.png or done2.png...etc.

### I have added few alphabets only. You can add your alphabets using following method.

* ####  If you want to add more alphabets follow following procedure for each alphabet.

   a. Write alphabet on plain white paper(with black pen). 
   
   b. Capture a photo with high quality camera.

   c. Crop the letter as close as possible from all sides.

   d. Remove white background using any background remover tool. [link](https://onlinepngtools.com/create-transparent-png)

   e. Resize the image and set its height to 160px maintaining the ratio. [link](https://play.google.com/store/apps/details?id=com.vinson.shrinker&hl=en_IN&gl=US)

   f. Suppose if the alphabet is capital 'A' save image as ca.png 

   g. else save it as a.png

   h. If it is any special symbol follow convention from the `maincode.py` function `getname()`

        
### > Refer the `myfont` directory for more help

## Updates

1. Need help to add tables in Output
