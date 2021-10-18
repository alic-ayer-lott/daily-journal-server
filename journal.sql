CREATE TABLE `Entries` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`concept`	TEXT NOT NULL,
	`entry`	TEXT NOT NULL,
	`date`	TEXT NOT NULL,
	`mood_id`	INTEGER NOT NULL
    FOREIGN KEY(`mood_id`) REFERENCES `Entry`(`id`)
);

CREATE TABLE `Mood` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `label`    TEXT NOT NULL,
)


INSERT INTO `Entries` VALUES (null, "Python", "I feel like I am getting the hang of this.", "10/18/2021", 1);
INSERT INTO `Entries` VALUES (null, "SQL", "I like using SQL.", "10/15/2021", 2);
INSERT INTO `Entries` VALUES (null, "SQL", "It is making data easier to understand.", "10/13/2021", 3);

INSERT INTO `Mood` VALUES (1, "Happy");
INSERT INTO `Mood` VALUES (2, "Excited");
INSERT INTO `Mood` VALUES (3, "Growth Mindset");
INSERT INTO `Mood` VALUES (4, "Sad")
