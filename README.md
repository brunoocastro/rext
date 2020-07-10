# REXT

*Text Remover Library*


A Python library to remove text from images


    - V 1.0


First version of this software thats object is remove text from specific images of an competition dataset

## Uses

### As Script:
    - Use rext.py -h to see how to use this script


    - You can call this script by terminal with this command line:
        -  OBS: Without '<' '>'

        ```shell
        python3 rext.py -i <input_image>
        ```
        

### AS Library:
    - For library uses, import this Library and call the clean function passing an image as an argument. The return is a clean image.

        - Params: clean(image, show)
        - If show = True, you can see all processing

        ```python
        import rext.py

        img = X

        new_img = rext.clean(img)
        ```

## Demonstration
    Now we will see an demonstration of how it works:

### First Exemple
Any web image
    ![Original Image](/demonstration/ex1.png) 
    ![Final Image](/demonstration/new_ex1.png) 
    ![Processing Image](/demonstration/ex1_detais.png) 
    
### Second Exemple
Image from memebase.com
    ![Original Image](/demonstration/ex1.png) 
    ![Final Image](/demonstration/new_ex1.png) 
    ![Processing Image](/demonstration/ex1_detais.png) 