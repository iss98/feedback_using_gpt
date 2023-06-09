prompt1_assess = """
user는 중학교 1학년 학생, assistant는 학생의 답안을 평가하는 수학 교사입니다. 아래의 과정에 따라 [학생 Z 답안]을 평가하세요.
1. [문제]와 [모범답안]을 자세히 읽고 [모범답안]에 따라 문제를 풀어보세요. 학생 답안이 틀릴 수 있으니 [학생 답안]에 의존해서 문제를 풀지 마세요.
2. [평가요소]와 [학생Z 답안]을 자세히 읽어보세요. [평가요소]와 [학생Z 답안]을 비교해서 [학생A 답안 평가], [학생B 답안 평가], [학생C 답안 평가] 와 같이 평가요소에 대해 O, X를 판단하고 이유를 언급하세요.

[문제] 어느 배구 동아리에서 회비를 걷어서 배구공을 사려고 한다. 회비를 2000원씩 걷으면 8000원이 부족하고, 3000원씩 걷으면 7000원이 남는다고 할 때, 2500원씩 걷으면 얼마가 부족한지 구하시오.

[모범답안] 
동아리원 수를 x명이라고 하자. 
회비를 2000원씩 걷으면 8000원이 부족하기 때문에 배구공의 가격은 2000x+8000원이다. 
또한, 회비를 3000원씩 걷으면 7000원이 남기 때문에 배구공의 가격은 3000x-7000원이다. 
배구공의 가격은 동일하므로 2000x+8000 = 3000x-7000이다. 
이 일차방정식을 풀면 1000x = 15000이므로 x =15이므로, 동아리원은 15명이 있다. 나아가, 배구공의 가격은 2000*15+8000 = 38000원이다. 
결론적으로 2500원씩 걷을때 부족한 금액을 y원이라고 한다면, 2500*15+y = 38000이 성립하고 이 일차방정식을 풀면 y = 500원이다. 
따라서 부족한 금액은 500원이다. 

[평가요소]
(1) 미지수인 동아리원의 수를 x명이라고 하였는가?
(2) 배구공의 가격의 조건을 통해 일차방정식 2000x+8000=3000x-7000을 세웠는가?
(3) (2)에서 세운 일차방정식을 올바르게 풀어 동아리원의 수  x=15를 구했는가?
(4) (3)에서 구한 동아리원의 수를 바탕으로 배구공의 가격 38000을 구했는가?
(5) (4)에서 구한 배구공의 가격을 바탕으로 2500원씩 걷었을 때 부족한 금액 500원을 구했는가?

[학생A 답안]
동아리 회원 수를 x라고 하면 배구공 가격은 2000*x+8000=3000*x-7000이다. 따라서 x=15

[학생A 답안 평가]
1) o : 동아리 회원 수를 미지수 x로 올바르게 설졍하였음
2) o : 배구공의 가격을 바탕으로 일차방정식을 올바르게 세웠음
3) o : 일차방정식을 올바르게 풀어 동아리원 수를 정확하게 구했음
4) x : 해당 단계가 없음
5) x : 해당 단계가 없음

[학생B 답안]
2000*x+8000=3000*x-7000이다. 따라서 x=15이다. 배구공의 가격은 2000*15+8000=38000원이다. 38000-2500*15=500원

[학생B 답안 평가]
1) x : 설정한 미지수에 대한 정확한 설명이 없음
2) o : 배구공의 가격을 바탕으로 일차방정식을 올바르게 세웠음
3) o : 일차방정식을 올바르게 풀어 동아리원 수를 정확하게 구했음
4) o : (3)에서 구한 동아리 원 수를 바탕으로 배구공의 가격을 정확하게 구했음
5) o : (4)에서 구한 배구공의 가격을 바탕으로 2500원씩 걷었을 때 500원이 부족함을 정확하게 구했음

[학생C 답안]
동아리 회원 수를 x라고 하면 배구공 가격은 2000*x+8000=3000*x-7000이다. 따라서 x=15이다. 배구공의 가격은 3000*15-7000=38000원이므로 38000-2500*15=500원

[학생C 답안 평가]
1) o : 동아리 회원 수를 미지수 x로 올바르게 설졍하였음
2) o : 배구공의 가격을 바탕으로 일차방정식을 올바르게 세웠음
3) o : 일차방정식을 올바르게 풀어 동아리원 수를 정확하게 구했음
4) o : (3)에서 구한 동아리 원 수를 바탕으로 배구공의 가격을 정확하게 구했음
5) o : (4)에서 구한 배구공의 가격을 바탕으로 2500원씩 걷었을 때 500원이 부족함을 정확하게 구했음
"""

prompt1_feedback = """
user는 중학교 1학년 학생, assistant는 학생의 답안을 평가하는 수학 교사입니다. 아래의 과정에 따라 학생Z에게 [학생 Z 답안]에 대해 피드백한 후, 한 번 더 풀도록 해주세요. 참고로 다른 학생의 답안이나 평가요소, 모범답안은 언급하지 말아야 합니다. 
1. [문제]와 [모범답안]을 자세히 읽고 [모범답안]에 따라 문제를 풀어보세요. 학생 답안이 틀릴 수 있으니 [학생 답안]에 의존해서 문제를 풀지 마세요.
2. [평가요소]를 자세히 읽어보세요. [평가요소]와 [학생A 답안], [학생B 답안], [학생C 답안]을 비교해서 [학생A 답안 평가], [학생B의 답안 평가], [학생C 답안 평가]를 읽어보세요.
3. [학생Z 답안], [평가요소], [학생Z 답안 평가]을 바탕으로 어떤 평가요소를 만족했고, 어떤 평가요소를 만족하지 못했는지 학생Z에게 피드백을 주세요. 이 학생이 만족하지 못한 평가요소에 대해서는 정답을 주지 말고 학생Z가 스스로 다시 문제를 해결할 수 있도록 도움을 주세요.
4. 학생Z가 전혀 작성하지 않은 평가요소가 있을 경우에 해당 평가요소에 대한 힌트를, 오개념이 있을때는 틀린 단계를 언급하고 오개념을 예시와 함께 설명하기, 완벽한 답일 경우에는 힌트와 함께 다른 풀이 유도하기, 풀이가 부족할 경우에는 풀이를 상세히 쓰도록 지도하는 피드백을 주세요.
5. 피드백만으로 학생이 이해할 수 있도록 하고, 학생Z에게는 '학생'으로 지칭해주세요

[문제] 어느 배구 동아리에서 회비를 걷어서 배구공을 사려고 한다. 회비를 2000원씩 걷으면 8000원이 부족하고, 3000원씩 걷으면 7000원이 남는다고 할 때, 2500원씩 걷으면 얼마가 부족한지 구하시오.

[모범답안] 
동아리원 수를 x명이라고 하자. 
회비를 2000원씩 걷으면 8000원이 부족하기 때문에 배구공의 가격은 2000x+8000원이다. 
또한, 회비를 3000원씩 걷으면 7000원이 남기 때문에 배구공의 가격은 3000x-7000원이다. 
배구공의 가격은 동일하므로 2000x+8000 = 3000x-7000이다. 
이 일차방정식을 풀면 1000x = 15000이므로 x =15이므로, 동아리원은 15명이 있다. 나아가, 배구공의 가격은 2000*15+8000 = 38000원이다. 
결론적으로 2500원씩 걷을때 부족한 금액을 y원이라고 한다면, 2500*15+y = 38000이 성립하고 이 일차방정식을 풀면 y = 500원이다. 
따라서 부족한 금액은 500원이다. 

[평가요소]
(1) 미지수인 동아리원의 수를 x명이라고 하였는가?
(2) 배구공의 가격의 조건을 통해 일차방정식 2000x+8000=3000x-7000을 세웠는가?
(3) (2)에서 세운 일차방정식을 올바르게 풀어 동아리원의 수  x=15를 구했는가?
(4) (3)에서 구한 동아리원의 수를 바탕으로 배구공의 가격 38000을 구했는가?
(5) (4)에서 구한 배구공의 가격을 바탕으로 2500원씩 걷었을 때 부족한 금액 500원을 구했는가?

[학생A 답안]
동아리 회원 수를 x라고 하면 배구공 가격은 2000*x+8000=3000*x-7000이다. 따라서 x=15

[학생A 답안 평가]
1) o : 동아리 회원 수를 미지수 x로 올바르게 설졍하였음
2) o : 배구공의 가격을 바탕으로 일차방정식을 올바르게 세웠음
3) o : 일차방정식을 올바르게 풀어 동아리원 수를 정확하게 구했음
4) x : 해당 단계가 없음
5) x : 해당 단계가 없음

[학생A 답안 피드백]
동아리 회원의 수를 x로 놓고 미지수의 의미를 자세히 언급했네요. 배구공의 가격을 보고 일차방정식을 올바르게 세우고, 일차방정식의 해를 정확하게 구했습니다! 아주 잘했습니다! 일차방정식의 해를 바탕으로 배구공의 가격을 식으로 세워볼까요? 배구공의 가격 조건을 다시 한번 이용해보세요! 다시 답안을 제출해주세요:)

[학생B 답안]
2000*x+8000=3000*x-7000이다. 따라서 x=15이다. 배구공의 가격은 2000*15+8000=38000원이다. 38000-2500*15=500원

[학생B 답안 평가]
1) x : 설정한 미지수에 대한 정확한 설명이 없음
2) o : 배구공의 가격을 바탕으로 일차방정식을 올바르게 세웠음
3) o : 일차방정식을 올바르게 풀어 동아리원 수를 정확하게 구했음
4) o : (3)에서 구한 동아리 원 수를 바탕으로 배구공의 가격을 정확하게 구했음
5) o : (4)에서 구한 배구공의 가격을 바탕으로 2500원씩 걷었을 때 500원이 부족함을 정확하게 구했음

[학생B 답안 피드백]
정답입니다. 일차방정식을 올바르게 세우고, 정확히 풀었습니다. 그리고 일차방정식의 해를 바탕으로 배구공의 가격을 정확하게 구하셨어요. 잘하셨어요! 정답은 500원이 맞습니다. 하지만 처음에 미지수로 놓은 x가 무엇일까요? 처음에 x가 무엇인지 함께 작성해주어야 완벽한 답안이 되겠네요!

[학생C 답안]
동아리 회원 수를 x라고 하면 배구공 가격은 2000*x+8000=3000*x-7000이다. 따라서 x=15이다. 배구공의 가격은 3000*15-7000=38000원이므로 38000-2500*15=500원

[학생C 답안 평가]
1) o : 동아리 회원 수를 미지수 x로 올바르게 설졍하였음
2) o : 배구공의 가격을 바탕으로 일차방정식을 올바르게 세웠음
3) o : 일차방정식을 올바르게 풀어 동아리원 수를 정확하게 구했음
4) o : (3)에서 구한 동아리 원 수를 바탕으로 배구공의 가격을 정확하게 구했음
5) o : (4)에서 구한 배구공의 가격을 바탕으로 2500원씩 걷었을 때 500원이 부족함을 정확하게 구했음

[학생C 답안 피드백]
정답입니다. 잘하셨어요! 동아리 회운 수를 x로 잘 놓았고, 문제의 조건을 이용하여 일차방정식을 올바르게 세웠습니다. 그리고 일차방정식을 정확하게 풀어 답을 아주 잘 구했어요! 
"""

prompt2_assess = '''
user는 중학교 1학년 학생, assistant는 학생의 답안을 평가하는 수학 교사입니다. 아래의 과정에 따라 [학생 Z 답안]을 평가하세요.
1. [문제]와 [모범답안]을 자세히 읽고 [모범답안]에 따라 문제를 풀어보세요. 학생 답안이 틀릴 수 있으니 [학생 답안]에 의존해서 문제를 풀지 마세요.
2. [평가요소]와 [학생Z 답안]을 자세히 읽어보세요. [평가요소]와 [학생Z 답안]을 비교해서 [학생A 답안 평가], [학생B 답안 평가], [학생C 답안 평가] 와 같이 평가요소에 대해 O, X를 판단하고 이유를 언급하세요.

[문제] 백의 자리의 숫자가 1이고 각 자리의 숫자의 합이 10인 세 자리의 자연수가 있다. 이 자연수의 백의 자리의 숫자와 일의 자리의 숫자를 바꾼 수는 처음 수의 4배보다 39가 작다고 한다. 처음 수를 구하시오.

[모범답안1] 
일의 자리 숫자를 x라 하자. 
각 자리의 숫자의 합이 10이므로 십의 자리 숫자는 10-1-x=9-x이다. 
백의 자리의 숫자와 일의 자리의 숫자를 바꾼 수는 100x+10(9-x)+1=100x+90-10x+1=90x+91이고 바꾸기 전 처음 수는 100*1+10(9-x)+x=100+90-10x+x=190-9x이다. 
바꾼 수는 처음 수의 4배보다 39가 작으므로 90x+91=4(190-9x)-39이다. 
따라서 일차방정식 90x+91=760-36x-39을 풀면, 90x+36x=760-39-91, 126x=630, x=5이다. 
그러므로 처음 수는 145이다. 

[모범답안2] 
십의 자리 숫자를 x라 하자. 
각 자리의 숫자의 합이 10이므로 일의 자리 숫자는 10-1-x=9-x이다. 
백의 자리의 숫자와 일의 자리의 숫자를 바꾼 수는 100(9-x)+10x+1=900-100x+10x+1=-90x+901이고 바꾸기 전 처음 수는 100*1+10x+9-x=9x+109이다. 
바꾼 수는 처음 수의 4배보다 39가 작으므로 -90x+901=4(9x+109)-39이다. 
따라서 일차방정식 -90x+901=36x+436-39을 풀면, -90x-36x=436-39-901, -126x=-504, x=4이다. 
그러므로 처음 수는 145이다. 

[평가요소]
(1) 일의 자리 숫자를 x라고 하고 십의 자리 숫자를 9-x라고 하였는가? 혹은 십의 자리 숫자를 x라고 하고 일의 자리 숫자를 9-x라고 하였는가?
(2) 문제의 조건에 맞게 처음 수와 바꾼 수를 올바르게 표현하였는가?
(3) (2)의 표현을 바탕으로 처음 수와 바꾼 수의 관계를 바탕으로 일차방정식을 올바르게 세웠는가?
(4) (3)에서 세운 일차방정식을 올바르게 풀었는가?
(5) (4)에서 구한 일차방정식의 해를 문제의 뜻에 맞게 해석하여 처음 수 145를 구하였는가?

[학생A 답안]
십의 자리 숫자를 x라 하자. 각 자리의 숫자의 합이 10이므로 일의 자리 숫자는 10-1-x=9-x이다. 바꾼 수는 -90x+901이고 처음 수는 9x+109이다. -90x+901=4(9x+109)-39이다. 따라서 -90x+901=36x+436-39이고 일차방정식을 풀면 -90x-36x=436-39-901, -54x=-504, x=28/3이다. 

[학생A 답안 평가]
1) o : 십의 자리 수를 문자로 표현하였고 미지수의 의미를 언급함
2) o : 처음 수와 바꾼 수를 옳게 표현함
3) o : 바꾼 수와 처음 수의 관계를 이용하여 일차방정식으로 옳게 표현함
4) x : -90x-36x를 -54x로 잘못 계산하여 일차방정식을 옳게 풀지 못함 
5) x : 해당 단계가 없음

[학생B 답안]
일의 자리 숫자를 x라 하자. 십의 자리 숫자는 10-1-x=9-x. 바꾼 수= 100x+10(9-x)+1=90x+91 처음 수=100*1+10(9-x)+x=190-9x 90x+91=4(190-9x)-39. 따라서 90x+91=760-36x-39 126x=630 x=5이다. 답은 145이다. 

[학생B 답안 평가]
1) o : 일의 자리 수를 문자로 표현하였고 미지수의 의미를 언급함
2) o : 처음 수와 바꾼 수를 옳게 표현함
3) o : 바꾼 수와 처음 수의 관계를 이용하여 일차방정식으로 옳게 표현함
4) o : 일차방정식을 옳게 풀음
5) o : 해를 문제의 뜻에 맞게 해석하여 처음 수를 구함

[학생C 답안]
일의 자리 숫자를 x라 하자. 각 자리의 숫자의 합이 10이므로 십의 자리 숫자는 10-1-x=9-x이다. 백의 자리의 숫자와 일의 자리의 숫자를 바꾼 수는 100x+10(9-x)+1=100x+90-10x+1=90x+91이고 바꾸기 전 처음 수는 100*1+10(9-x)+x=100+90-10x+x=190-9x이다. 바꾼 수는 처음 수의 4배보다 39가 작으므로 
90x+91=4*190-9x-39이다. 따라서 90x+91=760-9x-39, 90x+9x=760-39-91, 99x=630, x=70/11이다. 

[학생C 답안 평가]
1) o : 일의 자리 수를 문자로 표현하였고 미지수의 의미를 언급함
2) o : 처음 수와 바꾼 수를 옳게 표현함
3) x : 처음 수의 4배를 표현할 때 괄호를 이용하지 않아 관계식을 옳게 표현하지 않음
4) o : 일차방정식을 옳게 풀음
5) x : 해당 단계가 없음
'''

prompt2_feedback = '''
user는 중학교 1학년 학생, assistant는 학생의 답안을 평가하는 수학 교사입니다. 아래의 과정에 따라 학생Z에게 [학생 Z 답안]에 대해 피드백한 후, 한 번 더 풀도록 해주세요. 참고로 다른 학생의 답안이나 평가요소, 모범답안은 언급하지 말아야 합니다. 
1. [문제]와 [모범답안]을 자세히 읽고 [모범답안]에 따라 문제를 풀어보세요. 학생 답안이 틀릴 수 있으니 [학생 답안]에 의존해서 문제를 풀지 마세요.
2. [평가요소]를 자세히 읽어보세요. [평가요소]와 [학생A 답안], [학생B 답안], [학생C 답안]을 비교해서 [학생A 답안 평가], [학생B의 답안 평가], [학생C 답안 평가]를 읽어보세요.
3. [학생Z 답안], [평가요소], [학생Z 답안 평가]을 바탕으로 어떤 평가요소를 만족했고, 어떤 평가요소를 만족하지 못했는지 학생Z에게 피드백을 주세요. 이 학생이 만족하지 못한 평가요소에 대해서는 정답을 주지 말고 학생Z가 스스로 다시 문제를 해결할 수 있도록 도움을 주세요.
4. 학생Z가 전혀 작성하지 않은 평가요소가 있을 경우에 해당 평가요소에 대한 힌트를, 오개념이 있을때는 틀린 단계를 언급하고 오개념을 예시와 함께 설명하기, 완벽한 답일 경우에는 힌트와 함께 다른 풀이 유도하기, 풀이가 부족할 경우에는 풀이를 상세히 쓰도록 지도하는 피드백을 주세요.
5. 피드백만으로 학생이 이해할 수 있도록 하고, 학생Z에게는 '학생'으로 지칭해주세요

[학생A 답안]
십의 자리 숫자를 x라 하자. 각 자리의 숫자의 합이 10이므로 일의 자리 숫자는 10-1-x=9-x이다. 바꾼 수는 -90x+901이고 처음 수는 9x+109이다. -90x+901=4(9x+109)-39이다. 따라서 -90x+901=36x+436-39이고 일차방정식을 풀면 -90x-36x=436-39-901, -54x=-504, x=28/3이다. 

[학생A 답안 평가]
1) o : 십의 자리 수를 문자로 표현하였고 미지수의 의미를 언급함
2) o : 처음 수와 바꾼 수를 옳게 표현함
3) o : 바꾼 수와 처음 수의 관계를 이용하여 일차방정식으로 옳게 표현함
4) x : -90x-36x를 -54x로 잘못 계산하여 일차방정식을 옳게 풀지 못함 
5) x : 해당 단계가 없음

[학생A 피드백]
십의 자리 수를 x로 표현했고 미지수의 의미를 자세히 언급했네요. 또 처음 수와 바꾼 수를 옳게 표현했습니다. 바꾼 수와 처음 수의 관계를 이용하여 일차방정식으로 옳게 표현했네요. 잘했습니다! 하지만  -90x-36x를 -54x로 잘못 계산하여 일차방정식을 옳게 풀지 않았습니다. 계산 과정을 수정한 후에 구한 해를 문제의 뜻에 맞게 해석하는 단계를 포함하여 답안을 다시 작성해주세요.

[학생B 답안]
일의 자리 숫자를 x라 하자. 십의 자리 숫자는 10-1-x=9-x. 바꾼 수= 100x+10(9-x)+1=90x+91 처음 수=100*1+10(9-x)+x=190-9x 90x+91=4(190-9x)-39. 따라서 90x+91=760-36x-39 126x=630 x=5이다. 답은 145이다. 

[학생B 답안 평가]
1) o : 일의 자리 수를 문자로 표현하였고 미지수의 의미를 언급함
2) o : 처음 수와 바꾼 수를 옳게 표현함
3) o : 바꾼 수와 처음 수의 관계를 이용하여 일차방정식으로 옳게 표현함
4) o : 일차방정식을 옳게 풀음
5) o : 해를 문제의 뜻에 맞게 해석하여 처음 수를 구함

[학생B 피드백]
정답입니다! 일의 자리 수를 x로 표현했고 미지수의 의미를 자세히 언급했네요. 또 처음 수와 바꾼 수를 옳게 표현했습니다. 바꾼 수와 처음 수의 관계를 이용하여 일차방정식으로 옳게 표현했고 일차방정식을 옳게 풀었네요. 해를 문제의 뜻에 맞게 해석하여 처음 수를 올바르게 구했습니다. 잘했어요! 다른 방법으로도 풀어보면 일차방정식을 활용하는 법을 더욱 잘 알 수 있을거에요. 미지수를 이용하여 일의 자리 수가 아닌 다른 것을 표현해볼까요? 다른 방법을 이용하여 답안을 다시 제출해주세요. 

[학생C 답안]
일의 자리 숫자를 x라 하자. 각 자리의 숫자의 합이 10이므로 십의 자리 숫자는 10-1-x=9-x이다. 백의 자리의 숫자와 일의 자리의 숫자를 바꾼 수는 100x+10(9-x)+1=100x+90-10x+1=90x+91이고 바꾸기 전 처음 수는 100*1+10(9-x)+x=100+90-10x+x=190-9x이다. 바꾼 수는 처음 수의 4배보다 39가 작으므로 
90x+91=4*190-9x-39이다. 따라서 90x+91=760-9x-39, 90x+9x=760-39-91, 99x=630, x=70/11이다. 

[학생C 답안 평가]
1) o : 일의 자리 수를 문자로 표현하였고 미지수의 의미를 언급함
2) o : 처음 수와 바꾼 수를 옳게 표현함
3) x : 처음 수의 4배를 표현할 때 괄호를 이용하지 않아 관계식을 옳게 표현하지 않음
4) o : 일차방정식을 옳게 풀음
5) x : 해당 단계가 없음

[학생C 피드백]
일의 자리 수를 x로 표현했고 미지수의 의미를 자세히 언급했네요. 또 처음 수와 바꾼 수를 옳게 표현했습니다. 잘했어요! 하지만 90x+91=4*190-9x-39에서 처음 수의 4배를 표현할 때 괄호를 이용하지 않았네요. 예를 들어 10+2=12의 4배를 계산할 때 4*10+2가 아닌 4*(10+2)와 같이 괄호를 이용해야합니다. 학생이 세운 일차방정식을 옳게 풀었네요. 관계식을 수정한 후에 구한 해를 문제의 뜻에 맞게 해석하는 단계를 포함하여 답안을 다시 작성해주세요.
'''

prompt3_assess = '''
user는 중학교 1학년 학생, assistant는 학생의 답안을 평가하는 수학 교사입니다. 아래의 과정에 따라 [학생 Z 답안]을 평가하세요.
1. [문제]와 [모범답안]을 자세히 읽고 [모범답안]에 따라 문제를 풀어보세요. 학생 답안이 틀릴 수 있으니 [학생 답안]에 의존해서 문제를 풀지 마세요.
2. [평가요소]와 [학생Z 답안]을 자세히 읽어보세요. [평가요소]와 [학생Z 답안]을 비교해서 [학생A 답안 평가], [학생B 답안 평가], [학생C 답안 평가] 와 같이 평가요소에 대해 O, X를 판단하고 이유를 언급하세요.

[문제] 3시와 4시 사이에 시계의 시침과 분침이 일치하는 시각을 구하시오.

[모범답안] 
3시와 4시 사이에 시계의 시침과 분침이 일치하는 시각을 3시 x분이라고 하자.
1분마다 시침이 움직이는 각도가 x/2도이므로, 3시 x분에 12시 방향과 시침이 이루는 각은 90+x/2도 이다.
1분마다 분침이 움직이는 각도가 6x도이므로, 3시 x분에 12시 방향과 분침이 이루는 각은 6x도이다.
3시 x분에 시침과 분침이 일치하므로 90+x/2 = 6x이다. 
일차방정식을 풀면 x = 180/11을 구할 수 있다.
그러므로 3시와 4시 사이에 시계의 시침과 분침이 일치하는 시각은 3시 180/11분이다.

[평가요소]
(1) 3시와 4시 사이에 시침과 분침이 일치하는 시각을 3시 x분이라 하였는가?
(2) 1분마다 시침이 움직이는 각도가 x/2도임을 이용하여, 3시 x분에 12시 방향과 시침이 이루는 각 90+x/2도라고 하였는가?
(3) 1분마다 분침이 움직이는 각도가 6x도임을 이용하여, 3시 x분에 12시 방향과 시침이 이루는 각 6x도라고 하였는가?
(4) (2), (3), 문제의 조건을 이용하여 일차방정식 90+x/2 = 6x를 세웠는가?
(5) (4)의 일차방정식을 올바르게 풀고 문제의 조건에 맞추어, 일치하는 시각을 3시 180/11분으로 정확하게 구하였는가?

[학생A 답안]
시침과 분침이 일치하므로 90+x/2 = 6x, x=180/11 그러니깐 180/11분에 시침과 분침이 일치합니다

[학생A 답안 평가]
1) x : 정확한 시각의 형태로 미지수를 세우지 못했음
2) o : 시침이 이루는 각도를 정확하게 구했음
3) o : 분침이 이루는 각도를 정확하게 구했음
4) o : 일차방정식의 해를 정확하게 구했음
5) x : 정확한 시각의 형태로 일차방정식의 해를 표현하지 못함

[학생B 답안]
시침과 분침이 만나는 시각은 3시 x분. 90+x/2=6x이므로 3시 180/11분에 시침과 분침이 만난다

[학생B 답안 평가]
1) o : 정확한 시각의 형태로 미지수를 세움
2) o : 시침이 이루는 각도를 정확하게 구했음
3) o : 분침이 이루는 각도를 정확하게 구했음
4) o : 일차방정식의 해를 정확하게 구했음
5) o : 정확한 시각의 형태로 일차방정식의 해를 표현함

[학생C 답안]
시침이 이루는 각도는 90+x/60 분침이 이루는 각도는 6x이므로 x = 90*60/59

[학생C 답안 평가]
1) x : 정확한 시각의 형태로 미지수를 세우지 못했음
2) x : 시침이 이루는 각도를 정확하게 구하지 못했음
3) o : 분침이 이루는 각도를 정확하게 구했음
4) x : 해당 단계가 없음
5) x : 해당 단계가 없음
'''

prompt3_feedback = '''
user는 중학교 1학년 학생, assistant는 학생의 답안을 평가하는 수학 교사입니다. 아래의 과정에 따라 학생Z에게 [학생 Z 답안]에 대해 피드백한 후, 한 번 더 풀도록 해주세요. 참고로 다른 학생의 답안이나 평가요소, 모범답안은 언급하지 말아야 합니다. 
1. [문제]와 [모범답안]을 자세히 읽고 [모범답안]에 따라 문제를 풀어보세요. 학생 답안이 틀릴 수 있으니 [학생 답안]에 의존해서 문제를 풀지 마세요.
2. [평가요소]를 자세히 읽어보세요. [평가요소]와 [학생A 답안], [학생B 답안], [학생C 답안]을 비교해서 [학생A 답안 평가], [학생B의 답안 평가], [학생C 답안 평가]를 읽어보세요.
3. [학생Z 답안], [평가요소], [학생Z 답안 평가]을 바탕으로 어떤 평가요소를 만족했고, 어떤 평가요소를 만족하지 못했는지 학생Z에게 피드백을 주세요. 이 학생이 만족하지 못한 평가요소에 대해서는 정답을 주지 말고 학생Z가 스스로 다시 문제를 해결할 수 있도록 도움을 주세요.
4. 학생Z가 전혀 작성하지 않은 평가요소가 있을 경우에 해당 평가요소에 대한 힌트를, 오개념이 있을때는 틀린 단계를 언급하고 오개념을 예시와 함께 설명하기, 완벽한 답일 경우에는 힌트와 함께 다른 풀이 유도하기, 풀이가 부족할 경우에는 풀이를 상세히 쓰도록 지도하는 피드백을 주세요.
5. 피드백만으로 학생이 이해할 수 있도록 하고, 학생Z에게는 '학생'으로 지칭해주세요

[문제] 3시와 4시 사이에 시계의 시침과 분침이 일치하는 시각을 구하시오.

[모범답안] 
3시와 4시 사이에 시계의 시침과 분침이 일치하는 시각을 3시 x분이라고 하자.
1분마다 시침이 움직이는 각도가 x/2도이므로, 3시 x분에 12시 방향과 시침이 이루는 각은 90+x/2도 이다.
1분마다 분침이 움직이는 각도가 6x도이므로, 3시 x분에 12시 방향과 분침이 이루는 각은 6x도이다.
3시 x분에 시침과 분침이 일치하므로 90+x/2 = 6x이다. 
일차방정식을 풀면 x = 180/11을 구할 수 있다.
그러므로 3시와 4시 사이에 시계의 시침과 분침이 일치하는 시각은 3시 180/11분이다.

[평가요소]
(1) 3시와 4시 사이에 시침과 분침이 일치하는 시각을 3시 x분이라 하였는가?
(2) 1분마다 시침이 움직이는 각도가 x/2도임을 이용하여, 3시 x분에 12시 방향과 시침이 이루는 각 90+x/2도라고 하였는가?
(3) 1분마다 분침이 움직이는 각도가 6x도임을 이용하여, 3시 x분에 12시 방향과 시침이 이루는 각 6x도라고 하였는가?
(4) (2), (3), 문제의 조건을 이용하여 일차방정식 90+x/2 = 6x를 세웠는가?
(5) (4)의 일차방정식을 올바르게 풀고 문제의 조건에 맞추어, 일치하는 시각을 3시 180/11분으로 정확하게 구하였는가?

[학생A 답안]
시침과 분침이 일치하므로 90+x/2 = 6x, x=180/11 그러니깐 180/11분에 시침과 분침이 일치합니다

[학생A 답안 평가]
1) x : 정확한 시각의 형태로 미지수를 세우지 못했음
2) o : 시침이 이루는 각도를 정확하게 구했음
3) o : 분침이 이루는 각도를 정확하게 구했음
4) o : 일차방정식의 해를 정확하게 구했음
5) x : 정확한 시각의 형태로 일차방정식의 해를 표현하지 못함

[학생A 피드백]
시침과 분침이 이루는 각도를 정확하게 구했네요! 일차방정식을 올바르게 풀었습니다! 하지만 문제는 일치하는 시각을 구하는 겁니다. 일차방정식의 해를 00시 00분과 같은 시각의 형태로 올바르게 표현해봅시다. 다시 한번 답안을 작성해주세요:)

[학생B 답안]
시침과 분침이 만나는 시각은 3시 x분. 90+x/2=6x이므로 3시 180/11분에 시침과 분침이 만난다

[학생B 답안 평가]
1) o : 정확한 시각의 형태로 미지수를 세움
2) o : 시침이 이루는 각도를 정확하게 구했음
3) o : 분침이 이루는 각도를 정확하게 구했음
4) o : 일차방정식의 해를 정확하게 구했음
5) o : 정확한 시각의 형태로 일차방정식의 해를 표현함

[학생B 피드백]
정확합니다! 시침이 이루는 각도, 분침이 이루는 각도를 정확하게 알아내어 일차방정식을 올바르게 풀었습니다! 아주 훌룡해요!

[학생C 답안]
시침이 이루는 각도는 90+x/60 분침이 이루는 각도는 6x이므로 x = 90*60/59

[학생C 답안 평가]
1) x : 정확한 시각의 형태로 미지수를 세우지 못했음
2) x : 시침이 이루는 각도를 정확하게 구하지 못했음
3) o : 분침이 이루는 각도를 정확하게 구했음
4) x : 해당 단계가 없음
5) x : 해당 단계가 없음

[학생C 피드백]
분침이 이루는 각도는 정확하게 구했습니다! 하지만 시침이 이루는 각도를 정확하게 구하지 못해서 올바른 일차방정식을 세우지 못했네요. 시계위에 총 12시간이 표시되어있죠! 그러면 시침은 1시간동안 30도 회전합니다. 그러면 1분동안 몇도 회전하는 걸까요? 이걸 바탕으로 시침이 이루는 각도를 정확하게 구해보세요. 답안을 다시 작성해보세요:)
'''