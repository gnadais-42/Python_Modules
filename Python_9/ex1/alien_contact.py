from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime


class ContactType(Enum):
    RADIO: str = "radio"
    VISUAL: str = "visual"
    PHYSICAL: str = "physical"
    TELEPATHIC: str = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = None
    is_verified: bool = False

    @model_validator(mode='after')
    def check_id(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC" (Alien Contact)')
        return self
    
    @model_validator(mode='after')
    def check_physical_contacts(self) -> "AlienContact":
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        return self
    
    @model_validator(mode='after')
    def check_telepathic_contacts(self) -> "AlienContact":
        if self.contact_type == ContactType.TELEPATHIC \
        and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")
        return self
    
    @model_validator(mode='after')
    def check_strong_signals(self) -> "AlienContact":
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError("Strong signals (> 7.0) should include received messages")
        return self
    

def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    ac1 = AlienContact(
        contact_id="AC_2024_001",
        contact_type= ContactType.RADIO,
        location="Area 51, Nevada",
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        timestamp=datetime.now(),
        is_verified=True
    )
    print(
        "ID:", ac1.contact_id,
        "\nType:", ac1.contact_type,
        "\nLocation:", ac1.location,
        "\nSignal:", ac1.signal_strength,
        "\nDuration:", ac1.duration_minutes,
        "\nWitnesses:", ac1.witness_count,
        "\nMessage:", ac1.message_received
    )

    print("\n======================================")
    try:
        ac2 = AlienContact(
            contact_id="AC_2024_001",
        contact_type= ContactType.TELEPATHIC,
        location="Area 51, Nevada",
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=2,
        message_received="Greetings from Zeta Reticuli",
        timestamp=datetime.now(),
        is_verified=True
        )
    except ValidationError as e:
        print(f"Expected validation error:\n{e.errors()[0]['msg']}")


if __name__ == "__main__":
    main()