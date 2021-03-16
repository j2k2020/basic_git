# Git [파일/폴더] 변경사항 반영하기



### (1) `git 파일 수정`

######  -> github에 잘 못 올라간 파일 목록을 삭제하고 싶어서 찾아봄. 항상 흔치 않은 오류를 일으켜서 문제가 많이 복잡해짐;; 목록 삭제 이유는 잦은 커밋으로 목록이 정리가 되지 않아서 삭제를 진행 함.



>* 로컬 저장소 & 원격 저장소에서 `파일`/`폴더` 삭제하기
>
>  
>
>```sh
>$ git rm [파일/폴더명] //로컬 저장소와 원격 저장소 모두에서 파일 삭제
>$ git commit -m "Delete" //버전관리에서 완전한 제거를 위해 반드시 commit을 해야 함
>$ git push origin master
>```
>
> 
>
>
>
>* 원격 저장소에서만 `파일`/`폴더 `삭제하기(로컬에선 삭제되지 않음)
>
>  위에 나온 로컬&원격을 같이 삭제하는 방법을 찾기 이전에 나는 로컬에서 먼저 삭제를 해버렸다.ㅠㅠ 그래서 github에 남은 목록을 제거하기 위해 이 방법을 사용했다.
>
>  
>
>```shell
>$ git rm -cached [파일/폴더명] //원격 저장소에서만 삭제됨
>rm '[파일/폴더명]'//위의 코드를 실행하면 이렇게 나온다.(정상인듯)
>//난 여기가 끝인줄 알고 커밋을 안해서 한참을 오류와 싸웠다ㅠ
>
>//커밋 진행하기
>$ git commit -m "remove" // commit 진행
>$ git push origin master // 여기까지 진행하고 github확인하니 목록이 정리됨^^     
>```

---

####  `*목록을 확인`

![screenshot](Git_update%20and%20delete.assets/0316-1615910168326.PNG)

원하는 상태로 목록이 정리되었다. 지우기 전 목록은 캡처를 못 떠서 없다ㅠ 대신 2줄에 있는 01_Github_TIL_.md의 파일명을 변경해보기~

---



### (2) `git 파일명 수정`



>* 로컬 저장소와 원격 저장소에 파일명 수정하기
>
>  
>
>```shell
>$ mv $ mv 01_Github_TIL_.md //이렇게 했더니 아래 오류가 나옴. 
>mv: missing destination file operand after '01_Github_TIL_.md'
>Try 'mv --help' for more information. 
>
>// --help의 도움을 받기로 함
>$ mv --help
>Usage: mv [OPTION]... [-T] SOURCE DEST //소스 DEST
>  or:  mv [OPTION]... SOURCE... DIRECTORY
>  or:  mv [OPTION]... -t DIRECTORY SOURCE...
>Rename SOURCE to DEST, or move SOURCE(s) to DIRECTORY. //'소스의 이름을 DEST로 바꾸거나, 소스를 디렉토리로 이동시킨다.'라고 이해 함;;
>
>$ mv 01_Github_TIL_.md -T 01_Github_TIL.md
>$ git commit -m "2nd TIL" //바로 커밋이 않되나보다;;
>On branch master
>Changes not staged for commit:
>  (use "git add/rm <file>..." to update what will be committed)
>  (use "git restore <file>..." to discard changes in working directory)
>        deleted:    01_Github_TIL_.md
>
>Untracked files:
>  (use "git add <file>..." to include in what will be committed)
>        01_Github_TIL.md
>
>no changes added to commit (use "git add" and/or "git commit -a")
>
>//내 선택은 use "git add"
>$ git add 01_Github_TIL.md
>
>$ git commit -m "2nd TIL"
>[master fea7824] 2nd TIL
> 1 file changed, 161 insertions(+)
> create mode 100644 01_Github_TIL.md
> 
>$ git push origin master
>```

---



#### `* 목록 확인(1)`

![screenshot](Git_update%20and%20delete.assets/0317_1-1615910186402.PNG)



##### 뭐가 잘 못 된걸까;;; 목록이 4줄이 되어버렸다!!!  로컬 저장소는 문제 없는데...



##### ![](Git_update%20and%20delete.assets/0317_2.PNG)



> * 다시 처음부터 목록 삭제 진행
>
> ```sh
> $ git rm --cached 01_Github_ 
> //여기서 Tab을 눌러보니 아래 지워야 할 파일명(01_Github_TIL_.md)이 나온다.
> 01_Github_CLI.md   01_Github_TIL.md   01_Github_TIL_.md
> 
> $ git rm --cached 01_Github_TIL_.md //실행
> $ git commit -m "Delete" //commit진행
>  $ git push origin master //push
> ```



#### `* 목록 확인(2)`

![](Git_update%20and%20delete.assets/0317_3.PNG)

원하는 목록으로 정리 끝~!!



오늘 Git과 Github를 배운지 첫날이라 아직은 모르는것 투성이지만, 재미있기는 하다!! 그리고 커밋을 할때는 수정하기가 힘드니 신중히 생각하고 해야 될 것 같다;; 다음엔 이런 오류는 만들지 않는 걸로~