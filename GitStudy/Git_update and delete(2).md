# Git [파일/폴더] 삭제하기



### (1) `git 파일 삭제`

######  -> 왜 삭제가 안될까? 지난번 방법으론 지운거 같은데; 그래서 다시 시도해봄



>*  `파일`/`폴더` 삭제하기
>
>  
>
>```java
>$ git rm [파일/폴더명] //로컬 저장소와 원격 저장소 모두에서 파일 삭제
>$ git commit -m "Delete" //버전관리에서 완전한 제거를 위해 반드시 commit을 해야 함
>$ git push origin master
>    
>    
>/*[해결방안]*/   
>//위에 방법이 먹히지 않아서, 로컬 저장소의 파일 다 지우고 내려 받기부터 다시 진행
> $ git clone "url주소"
> 
> $ git rm -r --cached [삭제원하는 파일/폴더명] //찾아보니 위에선 -r --cached 가 빠졌었음
> $ git commit -m "파일 삭제"
> $ git push origin master 
> //이렇게 진행하고 나니 원격저장소의 디렉토리(폴더)는 삭제되는데, 로컬저장소의 폴더는 그대로 있다.
> //일딴 삭제는 되었는데, 뭔가 찜찜.. git명령어 공부하는 김에 리눅스도 공부해봐야겠다;;
>```
>



