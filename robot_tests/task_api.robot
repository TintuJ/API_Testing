*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    https://jsonplaceholder.typicode.com

*** Test Cases ***

Get Users
    Create Session    api    ${BASE_URL}
    ${resp}=    GET On Session    api    /users
    Should Be Equal As Integers    ${resp.status_code}    200

Get Single User
    Create Session    api    ${BASE_URL}
    ${resp}=    GET On Session    api    /users/1
    Should Be Equal As Integers    ${resp.status_code}    200

Get Posts
    Create Session    api    ${BASE_URL}
    ${resp}=    GET On Session    api    /posts
    Should Be Equal As Integers    ${resp.status_code}    200

Create Post
    Create Session    api    ${BASE_URL}
    ${resp}=    GET On Session    api    /posts/1
    Should Be Equal As Integers    ${resp.status_code}    200