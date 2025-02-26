"use client"
import Stack from "@mui/material/Stack";
import Link from "@mui/material/Link";

const MenuLink = ({refLink, text, active}) => {
  return (
    <Stack
      direction="row"
      spacing={2}
      alignItems="center"
      sx={{paddingLeft: 4}}
    >
      <Link
        href={refLink}
        variant="h6"
        underline="none"
        color={active ? "#f08c00" : "text.primary"}
      >
        {text}
      </Link>
    </Stack>
  );
};

export default MenuLink;
