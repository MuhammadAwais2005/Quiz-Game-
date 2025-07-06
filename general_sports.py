import sqlite3

def create_database():
    
    conn = sqlite3.connect('general_sports_quiz.db')
    cursor = conn.cursor()
    
    # Drop table if it exists (optional)
    cursor.execute('DROP TABLE IF EXISTS questions')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        difficulty TEXT CHECK(difficulty IN ('easy', 'medium', 'difficult')),
        question_text TEXT NOT NULL,
        option1 TEXT NOT NULL,
        option2 TEXT NOT NULL,
        option3 TEXT NOT NULL,
        option4 TEXT NOT NULL,
        correct_answer INTEGER CHECK(correct_answer BETWEEN 1 AND 4)
    )
    ''')

    # Example list of questions – You need to expand each difficulty to 50 questions
    # Below only partial data is shown for illustration
    easy_questions = [
            ('easy', 'How many points is a field goal worth in American football?', '1', '2', '3', '4', 3),
            ('easy', 'What piece of equipment is used to hit the ball in tennis?', 'Glove', 'Stick', 'Racket', 'Club', 3),
            ('easy', 'How many strikes does a batter get in baseball before they are out (excluding fouls)?', 'Two', 'Three', 'Four', 'Five', 2),
            ('easy', 'What is the term for a score of zero in tennis?', 'Love', 'Deuce', 'Advantage', 'Nil', 1),
            ('easy', 'In basketball, how many points is a successful free throw worth?', 'One', 'Two', 'Three', 'Zero', 1),
            ('easy', 'What is the object of the game in golf?', 'To score the most points', 'To run the fastest', 'To hit the ball into the fewest holes', 'To knock out your opponent', 3),
            ('easy', 'How many players are on a standard basketball team on the court at one time?', 'Five', 'Six', 'Seven', 'Eight', 1),
            ('easy', 'What is the name of the event where many track and field events are contested?', 'The Derby', 'The Grand Prix', 'The Olympics', 'The World Series', 3),
            ('easy', 'In swimming, what is the term for moving your arms in a circular motion to propel yourself forward in freestyle?', 'Kick', 'Stroke', 'Glide', 'Float', 2),
            ('easy', 'What is the color of the center circle on a basketball court?', 'Red', 'Blue', 'White', 'Yellow', 3),
            ('easy', 'What is the term for a tied score at the end of a boxing match?', 'Knockout', 'Technical Knockout', 'Draw', 'Decision', 3),
            ('easy', 'What piece of protective gear do baseball catchers wear on their face?', 'Helmet', 'Mask', 'Goggles', 'Visor', 2),
            ('easy', 'In ice hockey, what is the object that players try to shoot into the net?', 'Ball', 'Puck', 'Sphere', 'Disc', 2),
            ('easy', 'How many innings are there in a standard baseball game?', 'Seven', 'Eight', 'Nine', 'Ten', 3),
            ('easy', 'What is the term for a perfect score in bowling?', 'Strike', 'Spare', 'Turkey', 'Perfect Game', 4),
            ('easy', 'What is the name of the race over a set distance with obstacles such as hurdles and water jumps?', 'Marathon', 'Sprint', 'Steeplechase', 'Relay', 3),
            ('easy', 'In which sport do players use clubs to hit a small ball into a series of holes on a course?', 'Tennis', 'Badminton', 'Golf', 'Croquet', 3),
            ('easy', 'What is the term for hitting the shuttlecock over the net in badminton?', 'Serve', 'Smash', 'Clear', 'Shot', 4),
            ('easy', 'How many sets does a player need to win to win a standard singles match in tennis (in major tournaments for men)?', 'One', 'Two', 'Three', 'Four', 3),
            ('easy', 'What is the name of the scoring system in volleyball where a point is scored on every rally?', 'Side-out scoring', 'Rally scoring', 'Traditional scoring', 'Point-per-serve', 2),
            ('easy', 'What is the term for illegally moving more than two steps with the ball in basketball without dribbling?', 'Traveling', 'Walking', 'Running', 'Stepping', 1),
            ('easy', 'What is the piece of equipment used to protect a boxer\'s hands?', 'Gloves', 'Pads', 'Wraps', 'Mittens', 1),
            ('easy', 'In track and field, what is a race where runners hand off a baton to each other?', 'Individual race', 'Distance race', 'Relay race', 'Hurdles', 3),
            ('easy', 'What is the term for a score of one over par on a golf hole?', 'Birdie', 'Par', 'Bogey', 'Eagle', 3),
            ('easy', 'What is the object hit in a game of cricket?', 'Ball', 'Puck', 'Shuttlecock', 'Sphere', 1),
            ('easy', 'How many bases are there on a baseball field?', 'Two', 'Three', 'Four', 'Five', 3),
            ('easy', 'What is the term for a successful shot in basketball that is worth three points?', 'Slam dunk', 'Layup', 'Three-pointer', 'Jump shot', 3),
            ('easy', 'In swimming, which stroke is also known as the butterfly?', 'Freestyle', 'Backstroke', 'Breaststroke', 'Butterfly', 4),
            ('easy', 'What is the name of the net used in volleyball?', 'Volley net', 'Sport net', 'High net', 'Game net', 1),
            ('easy', 'What is the term for knocking down all the pins with the first ball in bowling?', 'Spare', 'Strike', 'Double', 'Triple', 2),
            ('easy', 'What is the playing surface for tennis called?', 'Court', 'Field', 'Pitch', 'Rink', 1),
            ('easy', 'What is the term for a player who throws the ball to the batter in baseball?', 'Pitcher', 'Catcher', 'Infielder', 'Outfielder', 1),
            ('easy', 'In ice hockey, what is a penalty where a player trips an opponent with their stick or body?', 'Slashing', 'Hooking', 'Tripping', 'Cross-checking', 3),
            ('easy', 'What is the name of the event that determines the champion of the National Football League (NFL)?', 'World Series', 'Super Bowl', 'NBA Finals', 'Stanley Cup Finals', 2),
            ('easy', 'What is the term for hitting the ball directly over the net in volleyball without being blocked?', 'Spike', 'Dig', 'Set', 'Ace', 4),
            ('easy', 'What is the piece of equipment used to propel a swimmer through the water?', 'Oars', 'Paddles', 'Flippers', 'Skis', 3),
            ('easy', 'In basketball, what is it called when a player dribbles the ball with both hands at the same time?', 'Double dribble', 'Traveling', 'Palming', 'Carrying', 1),
            ('easy', 'What is the term for a score of two under par on a golf hole?', 'Birdie', 'Eagle', 'Bogey', 'Albatross', 2),
            ('easy', 'What is the name of the stick used in lacrosse?', 'Lacrosse stick', 'Crosse', 'Net stick', 'Catch stick', 2),
            ('easy', 'In track and field, what is the event where athletes throw a heavy spherical ball?', 'Discus', 'Javelin', 'Shot put', 'Hammer throw', 3),
            ('easy', 'What is the term for a successful hit in baseball that allows the batter to reach first base safely?', 'Home run', 'Triple', 'Double', 'Single', 4),
            ('easy', 'What is the name of the playing area in boxing?', 'Ring', 'Square', 'Circle', 'Arena', 1),
            ('easy', 'In ice hockey, what is a goal called?', 'Score', 'Point', 'Goal', 'Mark', 3),
            ('easy', 'What is the term for failing to make a first serve in tennis?', 'Fault', 'Let', 'Ace', 'Double fault', 1),
            ('easy', 'What is the standard number of frames in a bowling game?', 'Eight', 'Nine', 'Ten', 'Eleven', 3),
            ('easy', 'What is the term for a shot that goes directly into the basket in basketball without touching the rim or backboard?', 'Swish', 'Bank shot', 'Alley-oop', 'Fadeaway', 1),
            ('easy', 'What is the name of the small, white, hard ball used in table tennis?', 'Ping pong ball', 'Wiffle ball', 'Golf ball', 'Tennis ball', 1),
            ('easy', 'In track and field, what is a long-distance running race of 26.2 miles?', 'Sprint', 'Middle distance', 'Marathon', 'Hurdles', 3),
            ('easy', 'What is the term for a defensive play in volleyball where a player prevents the ball from crossing the net?', 'Spike', 'Set', 'Block', 'Dig', 3),
            ('easy', 'What is the piece of equipment that protects a baseball batter\'s head?', 'Helmet', 'Cap', 'Visor', 'Mask', 1),
        ]

    medium_questions =  [
    ('medium', 'Which country has won the most FIFA World Cup titles?', 'Germany', 'Italy', 'Brazil', 'Argentina', 3),
    ('medium', 'Who is the all-time top scorer in the UEFA Champions League?', 'Lionel Messi', 'Raul', 'Cristiano Ronaldo', 'Robert Lewandowski', 3),
    ('medium', 'In which year did the first modern Olympic Games take place?', '1886', '1896', '1904', '1912', 2),
    ('medium', 'Which tennis player has won the most Grand Slam singles titles?', 'Roger Federer', 'Rafael Nadal', 'Novak Djokovic', 'Margaret Court', 4),
    ('medium', 'Which NBA player has the most career points?', 'Kareem Abdul-Jabbar', 'LeBron James', 'Kobe Bryant', 'Michael Jordan', 2),
    ('medium', 'What is the maximum break possible in snooker?', '147', '155', '180', '200', 1),
    ('medium', 'Which country won the first ever Cricket World Cup in 1975?', 'Australia', 'England', 'West Indies', 'India', 3),
    ('medium', 'Which boxer was known as "The Greatest"?', 'Joe Frazier', 'Mike Tyson', 'Muhammad Ali', 'George Foreman', 3),
    ('medium', 'How many players are on a baseball team\'s starting lineup?', '7', '8', '9', '10', 3),
    ('medium', 'Which golfer has won the most major championships?', 'Tiger Woods', 'Jack Nicklaus', 'Arnold Palmer', 'Phil Mickelson', 2),
    ('medium', 'In what year was the first Super Bowl played?', '1965', '1967', '1969', '1971', 2),
    ('medium', 'Which country has won the most Olympic gold medals in athletics?', 'Russia', 'China', 'United States', 'Jamaica', 3),
    ('medium', 'Who holds the record for most home runs in MLB history?', 'Babe Ruth', 'Hank Aaron', 'Barry Bonds', 'Alex Rodriguez', 3),
    ('medium', 'Which sport uses the term "love" to mean zero?', 'Badminton', 'Tennis', 'Table Tennis', 'Squash', 2),
    ('medium', 'How many rings are on the Olympic flag?', '4', '5', '6', '7', 2),
    ('medium', 'Which country invented the sport of badminton?', 'China', 'England', 'India', 'Japan', 2),
    ('medium', 'In bowling, what is it called when you knock down all pins with two balls?', 'Strike', 'Spare', 'Turkey', 'Split', 2),
    ('medium', 'Which athlete has won the most Olympic medals of all time?', 'Usain Bolt', 'Carl Lewis', 'Michael Phelps', 'Larisa Latynina', 3),
    ('medium', 'What is the national sport of Canada?', 'Ice Hockey', 'Lacrosse', 'Curling', 'Baseball', 2),
    ('medium', 'Which team has won the most NBA championships?', 'Chicago Bulls', 'Los Angeles Lakers', 'Boston Celtics', 'Golden State Warriors', 3),
    ('medium', 'In which country was the sport of judo developed?', 'China', 'Korea', 'Japan', 'Thailand', 3),
    ('medium', 'Which Grand Slam tennis tournament is played on clay courts?', 'Wimbledon', 'US Open', 'Australian Open', 'French Open', 4),
    ('medium', 'What is the distance of a marathon in kilometers?', '40.2 km', '41.8 km', '42.2 km', '43.5 km', 3),
    ('medium', 'Which country has won the most Eurovision Song Contests?', 'Sweden', 'Ireland', 'United Kingdom', 'France', 2),
    ('medium', 'In American football, how many points is a touchdown worth?', '5', '6', '7', '8', 2),
    ('medium', 'Which sport uses terms like "eagle" and "birdie"?', 'Archery', 'Golf', 'Badminton', 'Horse Racing', 2),
    ('medium', 'Which country hosted the 2016 Summer Olympics?', 'China', 'Japan', 'Brazil', 'Russia', 3),
    ('medium', 'Who is the only boxer to defeat Muhammad Ali in his prime?', 'George Foreman', 'Joe Frazier', 'Sonny Liston', 'Ken Norton', 2),
    ('medium', 'Which of these is NOT a position in soccer?', 'Shortstop', 'Goalkeeper', 'Midfielder', 'Striker', 1),
    ('medium', 'Which country won the 2018 FIFA World Cup?', 'Germany', 'Brazil', 'France', 'Spain', 3),
    ('medium', 'In cricket, how many balls are in an over?', '4', '5', '6', '7', 3),
    ('medium', 'Which sport awards the Vince Lombardi Trophy?', 'Baseball', 'Basketball', 'American Football', 'Hockey', 3),
    ('medium', 'Which country has won the most Winter Olympic medals?', 'Canada', 'Norway', 'United States', 'Russia', 2),
    ('medium', 'Who was the first woman to run a marathon in under 2:20:00?', 'Paula Radcliffe', 'Grete Waitz', 'Joan Benoit', 'Tegla Loroupe', 1),
    ('medium', 'Which of these is NOT a Grand Tour in cycling?', 'Tour de France', 'Giro d\'Italia', 'Vuelta a España', 'Tour of California', 4),
    ('medium', 'Which NBA team did Michael Jordan play for?', 'Los Angeles Lakers', 'Chicago Bulls', 'Boston Celtics', 'Miami Heat', 2),
    ('medium', 'In tennis, what is a zero score called?', 'Nil', 'Nada', 'Love', 'Zero', 3),
    ('medium', 'Which country won the first Rugby World Cup in 1987?', 'South Africa', 'Australia', 'New Zealand', 'England', 3),
    ('medium', 'How many players are on a volleyball team?', '5', '6', '7', '8', 2),
    ('medium', 'Which sport uses a shuttlecock?', 'Squash', 'Badminton', 'Tennis', 'Pickleball', 2),
    ('medium', 'Who was the first golfer to win all four modern majors?', 'Ben Hogan', 'Gene Sarazen', 'Tiger Woods', 'Jack Nicklaus', 2),
    ('medium', 'Which country has won the most Davis Cup titles?', 'Australia', 'France', 'United States', 'Spain', 3),
    ('medium', 'In baseball, how many strikes make an out?', '1', '2', '3', '4', 3),
    ('medium', 'Which country hosted the 2012 Summer Olympics?', 'Beijing', 'London', 'Rio', 'Tokyo', 2),
    ('medium', 'Which NFL team has won the most Super Bowls?', 'Dallas Cowboys', 'New England Patriots', 'Pittsburgh Steelers', 'San Francisco 49ers', 3),
    ('medium', 'What is the maximum score in gymnastics?', '10', '15', '20', 'There is no maximum', 1),
    ('medium', 'Which sport uses the term "stymie"?', 'Croquet', 'Golf', 'Billiards', 'Bowling', 2),
    ('medium', 'Who was the first gymnast to score a perfect 10 in the Olympics?', 'Nadia Comăneci', 'Olga Korbut', 'Mary Lou Retton', 'Simone Biles', 1),
    ('medium', 'Which country won the 2019 Cricket World Cup?', 'Australia', 'India', 'England', 'New Zealand', 3),
    ('medium', 'In which sport would you perform a "fosbury flop"?', 'Swimming', 'Gymnastics', 'Track and Field', 'Diving', 3)
]

    difficult_questions =  [
    ('difficult', 'Which player has made the most appearances in the English Premier League?', 'Ryan Giggs', 'Frank Lampard', 'Gareth Barry', 'James Milner', 3),
    ('difficult', 'Which country hosted the 1974 FIFA World Cup?', 'Argentina', 'Mexico', 'West Germany', 'Spain', 3),
    ('difficult', 'Who is the only player to score in a World Cup final, European Cup final, and UEFA Cup final?', 'Diego Maradona', 'Zinedine Zidane', 'Gerd Müller', 'Ronaldo Nazário', 3),
    ('difficult', 'Which boxer retired with an undefeated 49-0 record?', 'Sugar Ray Leonard', 'Floyd Mayweather Jr.', 'Rocky Marciano', 'Muhammad Ali', 3),
    ('difficult', 'Which country won the first ever Rugby World Cup in 1987?', 'Australia', 'South Africa', 'New Zealand', 'England', 3),
    ('difficult', 'Who was the first African-American to play Major League Baseball?', 'Satchel Paige', 'Jackie Robinson', 'Larry Doby', 'Moses Fleetwood Walker', 4),
    ('difficult', 'Which tennis player holds the record for most consecutive weeks at world No. 1?', 'Roger Federer', 'Pete Sampras', 'Novak Djokovic', 'Ivan Lendl', 3),
    ('difficult', 'In which year was the first official international cricket Test match played?', '1844', '1877', '1896', '1909', 2),
    ('difficult', 'Which NBA team drafted Kobe Bryant?', 'Los Angeles Lakers', 'Charlotte Hornets', 'Philadelphia 76ers', 'Boston Celtics', 2),
    ('difficult', 'Who is the only player to win the FIFA World Cup as both player and manager?', 'Franz Beckenbauer', 'Mário Zagallo', 'Didier Deschamps', 'Johann Cruyff', 2),
    ('difficult', 'Which golfer was known as "The Golden Bear"?', 'Arnold Palmer', 'Gary Player', 'Jack Nicklaus', 'Tiger Woods', 3),
    ('difficult', 'Which country has won the most Thomas Cup (badminton) titles?', 'China', 'Indonesia', 'Malaysia', 'Denmark', 2),
    ('difficult', 'Who was the first gymnast to perform a perfect 10 in Olympic competition?', 'Olga Korbut', 'Nadia Comăneci', 'Mary Lou Retton', 'Simone Biles', 2),
    ('difficult', 'Which baseball player had a 56-game hitting streak?', 'Babe Ruth', 'Lou Gehrig', 'Joe DiMaggio', 'Ted Williams', 3),
    ('difficult', 'Which country won the first ever FIFA Women\'s World Cup in 1991?', 'Germany', 'Norway', 'United States', 'Sweden', 3),
    ('difficult', 'Who is the only player to win three Wimbledon titles in three different decades?', 'Pete Sampras', 'Roger Federer', 'Björn Borg', 'Novak Djokovic', 2),
    ('difficult', 'Which NFL team has the most Hall of Famers?', 'Green Bay Packers', 'Chicago Bears', 'Pittsburgh Steelers', 'Dallas Cowboys', 2),
    ('difficult', 'Who was the first NBA player to score 100 points in a single game?', 'Elgin Baylor', 'Kobe Bryant', 'Wilt Chamberlain', 'Michael Jordan', 3),
    ('difficult', 'Which country has won the most Olympic medals in weightlifting?', 'Russia', 'China', 'Bulgaria', 'United States', 2),
    ('difficult', 'Who is the only player to win the Ballon d\'Or while playing for a non-European club?', 'George Weah', 'Lionel Messi', 'Diego Maradona', 'Pelé', 1),
    ('difficult', 'Which tennis player holds the record for most Grand Slam singles titles in the Open Era?', 'Roger Federer', 'Rafael Nadal', 'Novak Djokovic', 'Margaret Court', 3),
    ('difficult', 'Which country has won the most Asian Games gold medals?', 'Japan', 'South Korea', 'China', 'India', 3),
    ('difficult', 'Who was the first NHL player to score 50 goals in 50 games?', 'Wayne Gretzky', 'Maurice Richard', 'Mario Lemieux', 'Bobby Hull', 2),
    ('difficult', 'Which Formula 1 driver has the most pole positions?', 'Michael Schumacher', 'Lewis Hamilton', 'Ayrton Senna', 'Sebastian Vettel', 2),
    ('difficult', 'Who is the only boxer to win world titles in eight different weight classes?', 'Floyd Mayweather Jr.', 'Manny Pacquiao', 'Oscar De La Hoya', 'Roy Jones Jr.', 2),
    ('difficult', 'Which country has won the most Paralympic gold medals?', 'China', 'United States', 'Great Britain', 'Australia', 1),
    ('difficult', 'Who was the first woman to run a marathon in under 2 hours and 20 minutes?', 'Grete Waitz', 'Paula Radcliffe', 'Joan Benoit', 'Tegla Loroupe', 2),
    ('difficult', 'Which NBA team has the longest playoff streak?', 'Boston Celtics', 'Los Angeles Lakers', 'San Antonio Spurs', 'Portland Trail Blazers', 3),
    ('difficult', 'Who is the only player to win the FIFA World Cup, UEFA Champions League, and Ballon d\'Or in the same year?', 'Lionel Messi', 'Zinedine Zidane', 'Ronaldo Nazário', 'Bobby Charlton', 1),
    ('difficult', 'Which country has won the most Commonwealth Games gold medals?', 'Canada', 'England', 'Australia', 'India', 3),
    ('difficult', 'Who was the first golfer to shoot 63 in a major championship?', 'Jack Nicklaus', 'Greg Norman', 'Johnny Miller', 'Tiger Woods', 3),
    ('difficult', 'Which NFL quarterback has the most career passing yards?', 'Peyton Manning', 'Tom Brady', 'Brett Favre', 'Drew Brees', 4),
    ('difficult', 'Who is the only tennis player to achieve the Golden Slam (all four majors plus Olympic gold)?', 'Steffi Graf', 'Serena Williams', 'Roger Federer', 'Novak Djokovic', 1),
    ('difficult', 'Which country has won the most EuroBasket (basketball) championships?', 'United States', 'Russia', 'Yugoslavia', 'Spain', 3),
    ('difficult', 'Who was the first NHL player to score 800 career goals?', 'Wayne Gretzky', 'Gordie Howe', 'Mario Lemieux', 'Jaromír Jágr', 1),
    ('difficult', 'Which country won the first ever ICC T20 World Cup in 2007?', 'Australia', 'India', 'Pakistan', 'West Indies', 2),
    ('difficult', 'Who is the only player to win NBA MVP and Defensive Player of the Year in the same season?', 'Michael Jordan', 'Hakeem Olajuwon', 'Kevin Garnett', 'Giannis Antetokounmpo', 1),
    ('difficult', 'Which country has won the most Sudirman Cup (badminton) titles?', 'China', 'Indonesia', 'South Korea', 'Denmark', 1),
    ('difficult', 'Who was the first driver to win the Formula 1 World Championship?', 'Juan Manuel Fangio', 'Alberto Ascari', 'Giuseppe Farina', 'Stirling Moss', 3),
    ('difficult', 'Which NBA player has the most career triple-doubles?', 'Magic Johnson', 'Jason Kidd', 'LeBron James', 'Russell Westbrook', 4),
    ('difficult', 'Who is the only player to score a hat-trick in a FIFA World Cup final?', 'Pelé', 'Geoff Hurst', 'Gerd Müller', 'Zinedine Zidane', 2),
    ('difficult', 'Which country has won the most World Athletics Championships medals?', 'Russia', 'United States', 'Kenya', 'Jamaica', 2),
    ('difficult', 'Who was the first NHL goalie to wear a mask in a game?', 'Glenn Hall', 'Jacques Plante', 'Terry Sawchuk', 'Ken Dryden', 2),
    ('difficult', 'Which tennis player has won the most French Open titles?', 'Björn Borg', 'Rafael Nadal', 'Chris Evert', 'Roger Federer', 2),
    ('difficult', 'Who is the only NFL team to complete a perfect season (win all games including Super Bowl)?', 'Pittsburgh Steelers', 'Miami Dolphins', 'New England Patriots', 'Chicago Bears', 2),
    ('difficult', 'Which country has won the most Fed Cup (tennis) titles?', 'United States', 'Australia', 'Czech Republic', 'Spain', 1),
    ('difficult', 'Who was the first NBA player to be named MVP of the All-Star Game?', 'Bob Pettit', 'Bill Russell', 'Wilt Chamberlain', 'Oscar Robertson', 1),
    ('difficult', 'Which country has won the most men\'s World Handball Championships?', 'France', 'Sweden', 'Germany', 'Russia', 1),
    ('difficult', 'Who is the only player to win the UEFA Champions League with three different clubs?', 'Clarence Seedorf', 'Samuel Eto\'o', 'Cristiano Ronaldo', 'Xabi Alonso', 1),
    ('difficult', 'Which country has won the most men\'s Volleyball World Championships?', 'Brazil', 'Russia', 'United States', 'Italy', 2),
    ('difficult', 'Who was the first woman to win an Olympic gold medal in marathon?', 'Grete Waitz', 'Joan Benoit', 'Rosa Mota', 'Naoko Takahashi', 2),
    ('difficult', 'Which NBA coach has won the most championships?', 'Pat Riley', 'Phil Jackson', 'Red Auerbach', 'Gregg Popovich', 2),
    ('difficult', 'Who is the only player to win the FIFA World Cup Golden Ball twice?', 'Lionel Messi', 'Diego Maradona', 'Zinedine Zidane', 'Ronaldo Nazário', 1)
]

    all_questions = easy_questions + medium_questions + difficult_questions

    cursor.executemany('''
    INSERT INTO questions (difficulty, question_text, option1, option2, option3, option4, correct_answer)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', all_questions)

    # Commit and close
    conn.commit()
    conn.close()
    print("Database 'general_sports_quiz.db' created successfully with 150 general questions!")

if __name__ == '__main__':
    create_database()
