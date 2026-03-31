This is my 1st Car price predection model with 2060 instance (rows) and  16 features (column) and my lable is predecting car_price using 
regression model like liner regression

If this model 1st i use feature Engineering and also use feature extraction for reducing the course of dimensionality by applying PCA
i use Pca but pca is not use full for this data becouse this data is very small when i use i get  72% predection this num is by glacing 1st look okay but when i think again but  if i remove pca what happend and when i remove i m surprised i get 82% predection now i understand what happend when u use pca on small dataset it give those column that contain big varinace  I give example - >


like 1st column contain 0.24 percent data and  2nd contain 0.84 then it only pick those column that contain  maximum varince


## For Miniconda setup on other laptop:

**Step 1:** Download Miniconda:
```
https://docs.anaconda.com/miniconda/


conda create -n ml100-day python=3.10
conda activate ml100-day
pip install -r requirements.txt

python app.py