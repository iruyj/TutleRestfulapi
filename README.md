# TutleRestfulapi

🐢 it쇼 거북목 치료 공장 Django-Api 서버

---

## 프로젝트 기획이유

> 요즘 많은 사람들이 컴퓨터, 스마트폰 등 여러 스마트 기기를 이용하면서 거북목이 발달되었습니다. 거북목 증후군의 급격한 발병증가의 원인을 찾아본 결과 스마트폰 사용뿐 아니라 평소 생활습관과 깊은 연관이 있습니다. 특히 학교생활을 하며 노트북, 컴퓨터 사용빈도가 많다보니 자연스럽게 구부러진 자세를 한 학생들의 모습을 볼 수 있습니다. 거북목 치료를 희망하는 학생들을 많지만 바쁜 일상 속 치료를 하기에 무리가 있습니다. 따라서 짧은 시간을 투자하여 쉽고 간단히 할 수 있는 스트레칭을 생각하였습니다
>
> [거북이치료공장] 웹사이트에서 제공하는 스트레칭을 하면서 자신의 평소 자세를 올바르게 교정할 수 있도록 거북목이 심한 사람들과 거북목을 미리 예방하고 싶은 사람들을 위해 [거북이치료공장]이라는 웹 서비스를 개발하게 되었습니다.


## 주요 기능 설명

----

- 유저 거북이
    - 유저이메일당 한개의 거북이 캐릭터생성가능
    - 해당 유저 정보 저장
```json
{
    "email": "email1234@gmail.com",
    "name": "trr",
    "num": 5
}
```
- 스트레칭 로그 기록
    - 해당 유저의 스트레칭 기록 저장
    - 로그 형식으로 기록됨

```json
{
  "id": 1,
  "created": "2022-06-05",
  "start": "14:43:01.735829",
  "end": "18:34:00",
  "stretch": 1,
  "status": 5,
  "user_email": "email1234@gmail.com"
}
```



## 1. 스트레칭 api 설명
<hr>

#### [ 제공 url ]
<table>
<tr style="background-color: #4b7656">
<th>기능</th>
<th>url</th>
<th>method</th>
</tr>
<tr>
<td>스트레칭 생성</td>
<td>http://107.21.77.37/cure/</td>
<td>POST</td>
</tr>
<tr>
<td>로그 전체조회</td>
<td>http://107.21.77.37/cure/</td>
<td>GET</td>
</tr>
<tr>
<td>해당 유저 로그조회</td>
<td>http://107.21.77.37/cure/user?user_email=[이메일]</td>
<td>GET</td>
</tr>
<tr>
<td>해당 날짜 로그조회</td>
<td>http://107.21.77.37/cure/today?user_email=[이메일]&date=[날짜]</td>
<td>GET</td>
</tr>
<tr>
<td>로그 상세보기</td>
<td>http://107.21.77.37/cure/[id]</td>
<td>GET</td>
</tr>
<tr>
<td>로그 수정</td>
<td>http://107.21.77.37/cure/[id]</td>
<td>PUT</td>
</tr>
<tr>
<td>로그 삭제</td>
<td>http://107.21.77.37/cure/[id]</td>
<td>POST</td>
</tr>

</table>

<hr>

#### [ json 데이터 ]

<table>
<tr style="background-color: #4b7656">
<th>이름</th>
<th>타입</th>
<th>설명</th>
</tr>

<tr>
<td style="text-decoration: underline">id</td>
<td>IntegerField</td>
<td>식별번호</td>
</tr>
<tr>
<td>created</td>
<td>DateField</td>
<td>생성일(자동)</td>
</tr>
<tr>
<td>start</td>
<td>TimeField</td>
<td>시작시간(자동)</td>
</tr>
<tr>
<td>end</td>
<td>TimeField</td>
<td>완료시간</td>
</tr>
<tr>
<td>stretch</td>
<td>IntegerField</td>
<td>스트레칭 번호</td>
</tr>
<tr>
<td>status</td>
<td>IntegerField</td>
<td>스트레칭 개수</td>
</tr>
<tr>
<td>user_email</td>
<td>EmailField</td>
<td>유저 이메일</td>
</tr>
</table>

## 2. 유저 거북이 api 설명

<hr>

#### [ 제공 url ]
<table>
<tr style="background-color: #4b7656">
<th>기능</th>
<th>url</th>
<th>method</th>
</tr>
<tr>
<td>거북이 생성</td>
<td>http://107.21.77.37/turtle/new</td>
<td>POST</td>
</tr>
<tr>
<td>거북이 전체조회</td>
<td>http://107.21.77.37/turtle/</td>
<td>GET</td>
</tr>
<tr>
<td>해당 유저 거북이조회</td>
<td>http://107.21.77.37/turtle/user?user_email=[이메일]</td>
<td>GET</td>
</tr>
<tr>
<td>거북이 데이터수정</td>
<td>http://107.21.77.37/turtle/user?user_email=[이메일]</td>
<td>PUT</td>
</tr>
<tr>
<td>거북이 삭제</td>
<td>http://107.21.77.37/turtle/user?user_email=[이메일]</td>
<td>GET</td>
</tr>
</table>

<hr>

#### [ json 데이터 ]

<table>
<tr style="background-color: #4b7656">
<th>이름</th>
<th>타입</th>
<th>설명</th>
</tr>
<tr>
<td>name</td>
<td>CharField</td>
<td>거북이이름</td>
</tr>
<tr>
<td>num</td>
<td>IntegerField</td>
<td>캐릭터번호</td>
</tr>
<tr>
<td style="text-decoration: underline">email</td>
<td>EmailField</td>
<td>사용자이메일</td>
</tr>
</table>
