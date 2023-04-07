# import logging

# 로그 레벨뒤에 저건 최소 단위이다.
# logging.basicConfig(level=logging.ERROR, format="%(asctime)s [%(levelname)s] %(message)s")
# # 앞쪽에 시간정보 중간의 로그네임 뒤에 메시지

# # debug < info < warning < error < critical
# logging.debug("아 이거 코드누가짰어")
# logging.info("자동화 수행 준비")
# logging.warning("이 스크립트는 조금 오래 되었습니다. 실행상에 문제가 있을 수 있습니다.")
# logging.error("에러가 발생하였습니다. 에러 코드는 ...")
# logging.critical("복구가 불가능한 심각한 문제가 발생했습니다.")

# 터미널과 파일에 함께 로그 남기기★★★★★
import logging
from datetime import datetime

# 시간 [로그레벨] 메시지 형태로 로그를 작성
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger()
# 로그 레벨 설정
logger.setLevel(logging.DEBUG)

# 스트림
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

# 파일
filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log") # mylogfile_202105211618
fileHandler = logging.FileHandler(filename, encoding="utf-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logger.debug("로그를 남겨보는 테스트를 진행합니다.")