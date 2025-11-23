from langchain_core.messages import HumanMessage, AIMessage
from src.chains.itenary_chain import generate_itenary
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException

logger = get_logger(__name__)

class Planner:
    def __init__(self):
        self.messages = []
        self.city = ""
        self.interests = []
        self.itenary = ""
        
        logger.info("Planner initialized")

    def set_city(self, city: str):
        try:
            self.city = city
            self.messages.append(HumanMessage(content=city) )
            logger.info(f"City set to {self.city}")
        except Exception as e:
            logger.error(f"Error setting city: {e}")
            raise CustomException(f"Error setting city: {e}")

    def set_interests(self, interests: str):
        try:
            interests_list = [ i.strip() for i in interests.split(",")]
            self.interests = interests_list
            self.messages.append(HumanMessage(content=interests) )
            logger.info(f"Interests set to {interests_list}")
        except Exception as e:
            logger.error(f"Error setting interests: {e}")
            raise CustomException(f"Error setting interests: {e}")

    def create_itenary(self):
        try:
            logger.info(f"Creating itenary for {self.city} with interests {self.interests}")
            itenary = generate_itenary(self.city, self.interests)
            self.itenary = itenary
            self.messages.append(AIMessage(content=itenary) )
            logger.info(f"Itenary generated: {self.itenary}")
            return itenary
        except Exception as e:
            logger.error(f"Error creating itenary: {e}")
            raise CustomException(f"Error creating itenary: {e}")
