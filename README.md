# kube



### visual studio Django port 고정해서 실행

1. 프로젝트 속성 (솔루션 속성 아님)
2. 디버그
3. 실행탭에 포트번호



### Django template extends tag added extra space on top

- 공백 문제가 생겼음
- 별짓을 다 해봐도 상단에 공백이 생기는 것을 막지못함
- 찾아보니 UTF-8 BOM 없음으로 인코딩을 바꾸라는게 있었음
- visual studio 상에는 그런게 없어서 notepad++ 이용해서 저장하니 잘됨