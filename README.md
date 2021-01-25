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

    a. Use **#** to switch to the new line
    
    b. Use **^^** to align the text to centre(Applies to the whole line)
    
    c. Use **->** for Tab(You can't use multiple spaces as this is whitespace collapsing)

3. Run the `maincode.py`

4. Output will be generated in `final` directory with name done1.png or done2.png...etc.

### I have added few alphabets only you can add your alphabets using following method.

If you want to add more alphabets follow following procedure for each alphabet:

        1.Write alphabet on plain white paper(with black pen). 

        2.Capture a photo with high quality camera.

        3.Crop the letter as close as possible from all sides.

        4.Remove white background using any background remover tool. [link](https://onlinepngtools.com/create-transparent-png)

        5.Resize the image and set its height to 160px maintaining the ratio. [link](https://play.google.com/store/apps/details?id=com.vinson.shrinker&hl=en_IN&gl=US)

        6.Suppose if the alphabet is capital 'A' save image as ca.png 

        7.else save it as a.png

        8.If it is any special symbol follow convention from the `maincode.py` function `getname()`
        
        > Refer the `myfont` directory for more help
