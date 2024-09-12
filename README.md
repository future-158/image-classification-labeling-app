## 기능 
streamlit에서 간단히 이미지 classification labeling 

## 화면

키보드 누르면 알아서 annotation 만들고 저장함

<video width="1024" height="1024" controls>
  <source src="assets/demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


## 장점

1. 키보드 지원

class  a,b,c,d,e,f,g를 1,2,3,4,5,6,7 숫자로 매핑하여 

예를 들어 숫자 5를 누르면,

자동으로 아래 annotation이 생성되어,
```json
{ 
    filename: <current image filename>,
    label: "e" # 숫자 5에 해당
}
```
이 artifact/ 폴더에 저장되며, 다음 이미지로 넘어감


2. 코드가 100줄 이내로 간단함


# 감사
streamlit-shortcuts 라이브러리 덕분에, 

아래 매핑만 지정해놓으면 
```python
shortcut2label = {'1': 'Convertible',
 '2': 'Coupe',
 '3': 'Hatchback',
 '4': 'Minivan',
 '5': 'Pickup',
 '6': 'SUV',
 '7': 'Sedan',
 '8': 'Sportscar',
 '9': 'Truck',
 '10': 'Wagon'}

add_keyboard_shortcuts(shortcut2label)
```

```python
if st.button("1"):
    # code here
    ...

키보를 1을 누르면 위 btn이 눌러진 것으로 실행됨 
```

# 설치


```bash
pip install streamlit-shortcuts
pip install datasets cffi
```

예시 이미지는 50장이 포함되어 있기때문에, 아래는 생략해도 됨
```bash
pip install datasets cffi
```



## Attribution
This project uses a subset of the Stanford Cars Dataset with BLIP captions from Hugging Face. The dataset is available at https://huggingface.co/datasets/roskyluo/stanford_cars_blip and is licensed under the Apache 2.0 License.
