# Git특강 2일차

<br/>

 ### 1. add 취소하기

> 실수로 git add를 했거나, add를 했지만 취소하고 싶은 경우에 사용한다.
> 현재 알고 있는 명령어는 2가지이다. 하나는 git Bash에서 가이드 해주는 명령어와 구글링한 명령어다.
>
> <br/>
>
> **1.git Bash 명령어**
>
> - "git restore --staged <file>..."
>
> ```shell
> $ git add test.md   //test.md 파일 add하기
> 
> $ git status        //현재 git상태 확인
> On branch master
> Changes to be committed:
>   (use "git restore --staged <file>..." to unstage) //가이드라인 확인
>                                     //'파일을 이전 단계로 회복시키다(되돌리다)'라고 이해함.
>         new file:   test.md  
>         
> $ git restore --staged test.md      //add취소하기(되돌리기)
> 
> $ git status     //add취소 후, 현재 git상태 확인
> On branch master
> Untracked files:  //추적되지 않은 파일이라고 하면 정상적으로 add전으로 돌아옴.
>   (use "git add <file>..." to include in what will be committed) 
>         README.md    
> ```
>
>  <br/>
>
> <br/>
>
> **2.구글링해서 본 명령어**
>
> * "git reset HEAD <file>..." 
>
> ```shell
> $ git add test.md   //test.md 파일 add하기
> 
> $ git status        //현재 git상태 확인
> On branch master
> Changes to be committed:
>   (use "git restore --staged <file>..." to unstage) //가이드라인 확인
>                                     //'파일을 이전 단계로 회복시키다(되돌리다)'라고 이해함.
>         new file:   test.md  
>         
> $ git reset HEAD  test.md      
> //구글링해서 본 명령어는 이렇게 사용하고 있었다.'헤드 파일을 재설정'(?)이라고 이해함;;;
> 
> $ git status     //add취소 후, 현재 git상태 확인
> On branch master
> Untracked files:  //추적되지 않은 파일이라고 하면 정상적으로 add전으로 돌아옴.
>   (use "git add <file>..." to include in what will be committed) 
>         README.md    
> ```
>
>   <br/>왜일까? 내 git Bash창에는  (use "git reset HEAD <file>..." to unstage)이런 가이드라인이 나오지 않는다. 혹시, 몰라서 add할 때 파일 여러개를 같이 해보기도 하고, commit을 하고나서 확인도해 보았지만 나오질 않는다. 아직 git입문 단계라서 저 두 명령어의 차이점을 모르겠다ㅠ 
>
>  좀 더 공부한 뒤에 차이점을 알게되면 업뎃해야겠다. 
>
> 참고로, 아래는 커밋 취소하는 방법이다. add이랑 너무 똑 같아서 짧게 정리해보았다.



<br/>

### 2. commit 취소하기

>* "git restore <file>..." : <선택파일>의 commit을 취소하고 되돌린다
>* $ git reset HEAD^  :  가장 최근의 commit을 취소하고 되돌린다

<br/>











