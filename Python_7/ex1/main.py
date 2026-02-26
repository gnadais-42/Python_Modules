from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def draw(deck: Deck) -> Card:
    type: str
    card = deck.draw_card()

    if isinstance(card, SpellCard):
        type = "Spell"
    elif isinstance(card, CreatureCard):
        type = "Creature"
    elif isinstance(card, ArtifactCard):
        type = "Artifact"
    else:
        card = "Unknown type"
    print("Drew:", card.name(), f"({type})")
    return card


def draw_and_play(deck: Deck) -> None:
    c_deck = deck.deck().copy()
    for _ in c_deck:
        drawn = draw(deck)
        print("Play result:", drawn.play({}), end='\n\n')


def main() -> None:
    print("=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    deck = Deck()
    deck.add_card(SpellCard(
        "Lightning Bolt",
        3,
        "Common",
        "Deal 3 damage to a target"
    ))
    deck.add_card(CreatureCard(
        "Fire Dragon",
        5,
        "Legendary",
        7, 5
    ))
    deck.add_card(ArtifactCard(
        "Mana Crystal",
        2,
        "Uncommon",
        "Permanent: +1 mana per turn",
        3
    ))
    deck.shuffle()
    print("Deck stats:", deck.get_deck_stats(), end='\n\n')
    print("Drawing and playing cards:\n")
    draw_and_play(deck)
    print("Polymorphism in action: "
          "Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
