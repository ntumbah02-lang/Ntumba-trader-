import './globals.css';

export const metadata = {
  title: 'NTUMBA TRADER',
  description: 'Multi-market trading platform by Héritier Ntumba',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
